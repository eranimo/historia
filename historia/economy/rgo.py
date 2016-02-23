from enum import Enum
from historia.enums.dict_enum import DictEnum
from historia.economy.resources import ResourceType

class RGOType(DictEnum):
    fish_farm = {
        'title': 'Fish Farm',
        'type': ResourceType.fish,
        'biome_restriction': None,
        'must_be_coast': True
    }

class RGO(object):
    def __init__(self, manager, location):
        """
        manager: Historia instance
        location: second-level country division
        """
        self.manager = manager
        self.location = location
