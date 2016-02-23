from enum import Enum
from historia.enums.dict_enum import DictEnum

class NeedType(Enum):
    basic_needs = 'Basic Needs'
    daily_needs = 'Daily Needs'
    luxury_needs = 'Luxury Needs'

class Needs(DictEnum):
    fish = {
        'title': 'Fish',
        'type': NeedType.basic_needs
    }
