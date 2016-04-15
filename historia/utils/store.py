import arrow
from copy import deepcopy as copy

class Store:
    def __init__(self, start_day):
        self.tick = start_day

        # current instances of the models in the store
        self.storage = {}

        # versions of the models at every day
        self.versions = {}
        self.versions[start_day] = {}

    def next_day(self):
        "Advances a day"
        self.tick = self.tick.replace(days=+1)
        self.versions[self.tick] = {}

    def add(self, model):
        "Adds model(s) to the store"
        if isinstance(model, list):
            for i in model:
                self.storage[i.id] = i
        else:
            self.storage[model.id] = model

    def update(self):
        "Updates each model in the store"
        for id_num, model in self.storage.items():
            self.versions[self.tick][id_num] = copy(model.export())

    def export(self):
        return {key.format("YYYY-MM-DD"): value for key, value in self.versions.items()}
