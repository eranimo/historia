from enum import Enum

class Attitude(Enum):
    none = 'None'
    hostile = 'Hostile'
    outraged = 'Outraged'
    threatened = 'Threatened'
    neutral = 'Neutral'
    friendly = 'Friendly'

class GovernmentType(Enum):
    monarchy = 'Monarchy'
    republic = 'Republic'
    theocracy = 'Theocracy'
