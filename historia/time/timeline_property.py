
class TimelineProperty(object):
    """
        A property that changes when the program's current_day changes.
        Allows a property to change over time

        | Day      | Value |
        |----------|-------|
        | 01,01,01 | "foo" |
        | 12,02,01 | "bar" |
    """
    def __init__(self, manager, timeline):

        self.manager = manager

        # a list of (Day, value) tuples
        self.timeline = timeline

    def get(self, get_day):
        """ Gets the value at a particular timeline day """
        for day, value in self.timeline:
            if day >= get_day:
                return value
        return self.timeline[-1][1]

    def set(self, day, value):
        """ Sets the value after this day """
        if type(day) is Day:
            self.timeline.append((day, value))
        else:
            raise TypeError('day must be an instance of Day')
