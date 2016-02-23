from enum import Enum
from historia.enums.dict_enum import DictEnum

class ResourceType(DictEnum):
    fish = {
        'title': 'Fish'
    }

class Resource(object):
    """
    Represents a resource stockpile
    """
    def __init__(self, resource_type, amount):
        """
        resource_type: REsourceType
        amount: amount of resources
        """
        self.manager = manager
        self.location = location
