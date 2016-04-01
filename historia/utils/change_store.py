import arrow
from copy import deepcopy as copy
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
echo = pp.pprint

class Change:
    def __init__(self, type, key, value=None):
        self.type = type
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value and self.type == other.type

    def __key__(self):
        return self.type, self.key, self.value

    def __hash__(self):
        return hash(self.__key__())

    def __repr__(self):
        return "<Change type='{}' key='{}' value='{}'".format(self.type, self.key, self.value)

    def export(self):
        return self.__dict__


def list_changes(old_list, new_list, key):
    changes = []
    key_string = lambda index: key + '[' + str(index) + ']'

    if len(old_list) == len(new_list): # list same length
        for index, value in enumerate(new_list):
            if value != old_list[index]:
                changes.append(Change('set_index', key_string(index), value))
    elif len(old_list) < len(new_list): # list got bigger
        for index, value in enumerate(new_list):
            if index < len(old_list):
                if value != old_list[index]:
                    changes.append(Change('set_index', key_string(index), value))
            else:
                changes.append(Change('set_index', key_string(index), value))
    else: # list got smaller
        for index, value in enumerate(old_list):
            if index < len(new_list):
                if value != new_list[index]:
                    changes.append(Change('set_index', key_string(index), value))
            else:
                changes.append(Change('set_index', key_string(index), None))
    return changes


def dict_changes(old_dict, new_dict):
    # print('compare', old_dict, new_dict)
    changes = []
    for old_key in old_dict.keys():
        if old_key not in new_dict.keys():
            changes.append(Change('delete', old_key))
    for new_key, new_value in new_dict.items():
        if new_key not in old_dict.keys():
            changes.append(Change('set', new_key, new_value))
        else:
            for old_key, old_value in old_dict.items():
                if new_key == old_key:
                    if new_value != old_value:
                        if isinstance(new_value, list):
                            changes.extend(list_changes(old_value, new_value, new_key))
                        else:
                            changes.append(Change('update', new_key, new_value))

    return changes


class ChangeStore:
    "A dictionary of models that reports the changes made to them within the last `tick`"
    def __init__(self, start_day):
        self.initial_tick = start_day
        self.tick = self.initial_tick
        self.store = {}


        self.change_log = {}
        self.change_log[self.initial_tick] = {}
        self.store_updates = {}
        self.store_updates[self.initial_tick] = {}

    def model_get(self, model):
        return copy(model.export())

    def extend(self, models):
        "Add a bunch of models"
        for m in models:
            self.add(m)

    def last_day(self):
        return self.tick.replace(days=-1)

    def add(self, model):
        "Add a new model to the store"
        self.store[model.id] = model
        changes = dict_changes({}, self.model_get(model))
        self.change_log[self.tick][model.id] = changes
        self.store_updates[self.tick][model.id] = self.model_get(model)

    def commit(self):
        "Commits changes and returns what models have changed within the last tick"
        # loop over every model, update if changed
        if self.tick == self.initial_tick:
            return self.change_log[self.initial_tick]

        for id_num, model in self.store.items():
            self.store_updates[self.tick][id_num] = self.model_get(model)

        # compile changes
        for id_num, model in self.store.items():
            try:
                last_model = self.store_updates[self.last_day()][id_num]
            except KeyError:
                last_model = {}
            current_model = self.model_get(model)
            if current_model != last_model:
                self.change_log[self.tick][id_num] = dict_changes(last_model, current_model)

        return self.change_log[self.tick]

    def next_day(self):
        self.tick = self.tick.replace(days=+1)
        self.change_log[self.tick] = {}
        self.store_updates[self.tick] = {}

    def export(self):
        return {key.format("YYYY-MM-DD"): value for key, value in self.change_log.items()}
