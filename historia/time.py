class CalendarError(Exception):
    pass

class Day:
    def __init__(self, day, month, year):
        if 1 <= day <= 30:
            self._day = day
        else:
            raise CalendarError('Days must be between 0 and 30')
        if 1 <= month <= 12:
            self._month = month
        else:
            raise CalendarError('Months must be between 0 and 12')
        if year >= 1:
            self._year = year
        else:
            raise CalendarError('Years must be positive')

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def stamp(self):
        return (self.day * 24) + (self.month * 720) + (self.year * 8640)

    def __lt__(self, other):
        return self.stamp < other.stamp

    def __le__(self, other):
        return self.stamp <= other.stamp

    def __gt__(self, other):
        return self.stamp > other.stamp

    def __ge__(self, other):
        return self.stamp >= other.stamp

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __ne__(self, other):
        return not self.__eq(other)

    def __key(self):
        return self.stamp

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return "<Calendar: type: {}, size: {}, id: {}>".format(self.type.title, self.size, self.id)

    def next():
        if self.day == 30:
            self.day = 1
            if self.month == 12:
                self.month = 1
            else:
                self.month += 1

class TimelineProperty:
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
        for day, value in timeline:
            if day <= get_day:
                return value
        return Exception('Day not found in timeline')

    def set(self, day, value):
        """ Sets the value after this day """
        self.timeline.append((day, value))
