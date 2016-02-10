from enum import Enum

class LogEvent(Enum):
    info = 'Simulation info'
    settlement = 'County settlement'

class HistoryLogger(object):

    def __init__(self, manager):
        self.items = []
        self.manager = manager

    def log(self, message, context, event=None):
        """
            Logs a message to the history logger with a context.
        """
        if event is None:
            event = LogEvent.info

        self.items.append({
            'date': self.manager.current_day,
            'event': event,
            'message': message,
            'context': context
        })

    def export(self, file_path):
        """ Export as JSON """
        pass
