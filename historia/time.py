from historia.errors import CalendarError

DAYS_IN_MONTH = 30
MONTHS_IN_YEAR = 12

MONTH_NAMES = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])


class Day(object):
    def __init__(self, day, month, year):
        if 1 <= day <= DAYS_IN_MONTH:
            self._day = day
        else:
            raise CalendarError('Days must be between 0 and 30')
        if 1 <= month <= MONTHS_IN_YEAR:
            self._month = month
        else:
            raise CalendarError('Months must be between 0 and 12')
        if year >= 1:
            self._year = year
        else:
            raise CalendarError('Years must be positive')

    def display(self):
        return '%s %s, year %s' % (MONTH_NAMES[self.month - 1], ordinal(self.day), self.year)

    def add(self, days=None, months=None, years=None):
        if days is not None:
            if days >= DAYS_IN_MONTH:
                self.day = days % DAYS_IN_MONTH + 1
                m = days // DAYS_IN_MONTH
                if m >= MONTHS_IN_YEAR:
                    self.month = m % MONTHS_IN_YEAR + 1
                    self.year += m // MONTHS_IN_YEAR
                else:
                    self.month += m
            else:
                self.day += days
        if months is not None:
            if months >= MONTHS_IN_YEAR:
                self.month = months % MONTHS_IN_YEAR + 1
                self.year += months // MONTHS_IN_YEAR
            else:
                self.month += months
        if years is not None:
            self.year += years
        return self

    # def subtract(self, days=None, months=None, years=None):
    #     if days is not None:
    #         if self.day - days <= 1:
    #             if self.month <= 1:
    #                 self.day = DAYS_IN_MONTH - days
    #                 self.month = MONTHS_IN_YEAR - 1
    #                 self.year -= 1
    #     if months is not None:
    #         if months - self.months < 1:
    #
    #     if years is not None:
    #         if self.year < 1:
    #             raise CalendarError()
    #         else:
    #             self.year -= years
    #     return self

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

    @property
    def stamp(self):
        return (self.day * 24) + (self.month * 720) + (self.year * 8640)

    def __add__(self, amount):
        self.day += amount
        return self

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
        return not self.__eq__(other)

    def __key__(self):
        return self.stamp

    def __hash__(self):
        return hash(self.__key__())

    def __str__(self):
        return "<Day: day={} month={} year={}>".format(self.day, self.month, self.year)

    def __repr__(self):
        return self.__str__()


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
