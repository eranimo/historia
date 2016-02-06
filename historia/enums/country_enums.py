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

class ProvinceTypes(Enum):
    province = 'Province'
    territory = 'Territory'
    colonial = 'Colonial'

class EthnicComposition(Enum):
    multiethnic = 'Multiethnic'
    nation_state = 'Nation State'

class GovernmentTypes(Enum):
    republic = 'Republic'
    monarchy = 'Monarchy'
    theocracy = 'Theocracy'
