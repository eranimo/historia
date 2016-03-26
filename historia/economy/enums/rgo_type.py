from enum import Enum

from historia.enums.dict_enum import DictEnum
from historia.economy.enums import Good
from historia.pops.enums.pop_type import PopType

class RGOType(DictEnum):
    __defaults__ = {
        'biomes': None,
        'must_be_coast': False
    }

    fish_farm = {
        'title': 'Fish Farm',
        'good': Good.fish,
        'base_production': 10,
        'worker_type': PopType.farmer
    }

    cattle_farm = {
        'title': 'Cattle Farm',
        'good': Good.meat,
        'base_production': 10,
        'worker_type': PopType.farmer
    }

    grain_farm = {
        'title': 'Farm',
        'good': Good.grain,
        'base_production': 10,
        'worker_type': PopType.farmer
    }

    fruit_farm = {
        'title': 'Fruit Farm',
        'good': Good.fruit,
        'base_production': 100,
        'worker_type': PopType.farmer
    }
    vegetable_farm = {
        'title': 'Vegetable Farm',
        'good': Good.vegetable,
        'base_production': 100,
        'worker_type': PopType.farmer
    }
    iron_mine = {
        'title': 'Iron Mine',
        'good': Good.iron,
        'base_production': 50,
        'worker_type': PopType.laborer
    }
    timber_lodge = {
        'title': 'Timber Lodge',
        'good': Good.timber,
        'base_production': 100,
        'worker_type': PopType.laborer
    }
    sheep_ranch = {
        'title': 'Sheep Ranch',
        'good': Good.wool,
        'base_production': 25,
        'worker_type': PopType.laborer
    }
    cotton_plantation = {
        'title': 'Cotton Plantation',
        'good': Good.cotton,
        'base_production': 25,
        'worker_type': PopType.farmer
    }
