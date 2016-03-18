from enum import Enum
from historia.enums.dict_enum import DictEnum

class HexEdge(Enum):
    east       = 'East'
    north_east = 'North East'
    north_west = 'North West'
    west       = 'West'
    south_west = 'South West'
    south_east = 'South East'


class HexType(Enum):
    water = 'Water'
    land = 'Land'
