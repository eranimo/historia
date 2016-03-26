from enum import Enum

class LogAction(Enum):
    set = "Set"
    extend = "Extend"
    add = "Add"
    remove = "Remove"

class HistoryLogger(object):

    def __init__(self, manager):
        self.items = {}
        self.manager = manager

    def log(self, model, change_dict, action=LogAction.set):
        """
            Logs a message to the history logger with a context.
        """
        day = self.manager.current_day.format("YYYY-MM-DD")
        data = {
            'type': model.__class__.__name__,
            'id': model.id,
            'change': change_dict,
            'action': action.name
        }
        try:
            self.items[day].append(data)
        except KeyError:
            self.items[day] = [data]

    def export(self):
        """ Export as JSON """
        return self.items
