from collections import namedtuple
from random import uniform

class PriceRange:
    "A range between two prices"

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def random(self):
        return round(uniform(self.low, self.high), 2)

    def mean(self):
        return self.low + self.high / 2
