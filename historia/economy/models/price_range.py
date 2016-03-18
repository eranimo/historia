from collections import namedtuple
from random import uniform

class PriceRange(namedtuple('PriceRange', 'low high')):
    "A range between two prices"
    def random(self):
        return round(uniform(self.low, self.high), 2)
