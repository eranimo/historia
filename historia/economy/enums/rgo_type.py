from enum import Enum

from historia.enums.dict_enum import DictEnum
from historia.economy.enums import Resource
from historia.pops.enums.pop_type import PopType

class RGOType(DictEnum):
    __defaults__ = {
        'biomes': None,
        'must_be_coast': False
    }

    fish_farm = {
        'title': 'Fish Farm',
        'type': Resource.fish,
        'base_production': 10,
        'worker_type': PopType.farmer
    }

    grain_farm = {
        'title': 'Farm',
        'type': Resource.grain,
        'base_production': 10,
        'worker_type': PopType.farmer
    }

    fruit_farm = {
        'title': 'Fruit Farm',
        'type': Resource.fruit,
        'base_production': 100,
        'worker_type': PopType.farmer
    }
    vegetable_farm = {
        'title': 'Vegetable Farm',
        'type': Resource.vegetable,
        'base_production': 100,
        'worker_type': PopType.farmer
    }
    iron_mine = {
        'title': 'Iron Mine',
        'type': Resource.iron,
        'base_production': 50,
        'worker_type': PopType.laborer
    }
    timber_lodge = {
        'title': 'Timber Lodge',
        'type': Resource.timber,
        'base_production': 100,
        'worker_type': PopType.laborer
    }
    sheep_ranch = {
        'title': 'Sheep Ranch',
        'type': Resource.wool,
        'base_production': 25,
        'worker_type': PopType.laborer
    }
    cotton_plantation = {
        'title': 'Cotton Plantation',
        'type': Resource.cotton,
        'base_production': 25,
        'worker_type': PopType.farmer
    }
