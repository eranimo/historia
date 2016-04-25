from historia.enums import HexEdge, HexType
from historia.world.biome import Biome
from historia.utils import unique_id

class Hex:
    """
        Smallest unit on the map
        Horizontal hexagons
        Modified version from Hexgen
    """
    def __init__(self, world_map, data):
        self.id = unique_id('he')
        self.world_map = world_map
        self.x = data.get('x')
        self.y = data.get('y')
        self.altitude = data.get('altitude')

        edges = data.get('edges')
        self.map_data = data

        self.biome = Biome[data.get('biome').get('name')]

        self.edge_east = edges.get('east')
        self.edge_north_east = edges.get('north_east')
        self.edge_north_west = edges.get('north_west')
        self.edge_west = edges.get('west')
        self.edge_south_west = edges.get('south_west')
        self.edge_south_east = edges.get('south_east')

        self.edges = [
            self.edge_east,
            self.edge_north_east,
            self.edge_north_west,
            self.edge_west,
            self.edge_south_west,
            self.edge_south_east
        ]

        self.has_river = False
        self.is_coast = False
        for e in self.edges:
            if e.get('is_river'):
                self.has_river = True
            if e.get('is_coast'):
                self.is_coast = True

        self.owner = None
        self._neighbors = None

        self.natural_resources = []

    def has_natural_resource(self, nresource):
        return nresource in self.natural_resources

    @property
    def owned(self):
        """ Is this hex owned by a province? """
        return self.owner is not None

    @property
    def type(self):
        """ Return the type of the Hex """
        if self.altitude < self.world_map.details.get('sea_level'):
            return HexType.water
        return HexType.land

    @property
    def is_land(self):
        return self.type is HexType.land

    @property
    def is_water(self):
        return self.type is HexType.water

    @property
    def favorability(self):
        """
        Hexes with a higher settlement score will be settled first.

        Criteria for a higher score:
            - rivers
            - lots of water
            - fertile land
            - resources
        """
        if self.is_water:
            return 0
        score = 0
        if self.is_coast:
            score += 30
        if self.has_river:
            score += 80
        score += self.biome.base_favorability
        return score

    def __repr__(self):
        return "<Hex: x={} y={} altitude={} biome={} is_land={} owner={}>".format(self.x, self.y, self.altitude, self.biome.title, self.is_land, self.owner)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __key__(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key__())

    @property
    def hex_east(self):
        """ Returns the hex to the East or None if end of map"""
        if self.y == self.world_map.size-1:
            return self.world_map.find_hex(self.x, 0)
        else:
            return self.world_map.find_hex(self.x, self.y + 1)

    @property
    def hex_west(self):
        """ Returns the hex to the West or None if end of map"""
        if self.y == 0:
            return self.world_map.find_hex(self.x, self.world_map.size-1)
        else:
            return self.world_map.find_hex(self.x, self.y - 1)

    @property
    def hex_north_west(self):
        """ Returns the hex to the north west"""
        if self.x == 0:  # top of map
            return self.world_map.find_hex(0, round(self.y / -1 + self.world_map.size-1))
        elif self.y == 0 and self.x % 2 == 0:  # left of map and even
            return self.world_map.find_hex(self.x - 1, self.world_map.size-1)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x - 1, self.y - 1)
            else:
                return self.world_map.find_hex(self.x - 1, self.y)

    @property
    def hex_north_east(self):
        """ Returns the hex to the North East or None if end of map"""
        if self.x == 0:  # top of map
            return self.world_map.find_hex(0, round(self.y / -1 + self.world_map.size-1))
        elif self.y == self.world_map.size-1 and self.x % 2 == 1:  # right of map and x is odd
            return self.world_map.find_hex(self.x - 1, 0)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x - 1, self.y)
            else:
                return self.world_map.find_hex(self.x - 1, self.y + 1)

    @property
    def hex_south_west(self):
        """ Returns the hex to the South West or None if end of map"""
        if self.x == self.world_map.size-1:  # bottom of map
            return self.world_map.find_hex(self.world_map.size-1, round(self.y / -1 + self.world_map.size-1))
        elif self.y == 0 and self.x % 2 == 1:  # left of map and x is odd
            return self.world_map.find_hex(self.x + 1, self.world_map.size-1)
        elif self.y == 0 and self.x % 2 == 0:  # left of map and x is even
            return self.world_map.find_hex(self.x + 1, 0)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x + 1, self.y - 1)
            else:
                return self.world_map.find_hex(self.x + 1, self.y)

    @property
    def hex_south_east(self):
        """ Returns the hex to the South East or None if end of map"""
        if self.x == self.world_map.size-1:  # bottom of map
            return self.world_map.find_hex(self.world_map.size-1, round(self.y / -1 + self.world_map.size-1))
        elif self.y == self.world_map.size-1 and self.x % 2 == 1:  # right of map and x is odd
            return self.world_map.find_hex(self.x + 1, 0)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x + 1, self.y)
            else:
                return self.world_map.find_hex(self.x + 1, self.y + 1)

    @property
    def neighbors(self):
        "Surrounding hexes with HexEdge enums"
        if self._neighbors is not None:
            return self._neighbors
        else:
            self._neighbors = [
                (self.hex_east, HexEdge.east),
                (self.hex_south_east, HexEdge.south_east),
                (self.hex_south_west, HexEdge.south_west),
                (self.hex_west, HexEdge.west),
                (self.hex_north_west, HexEdge.north_west),
                (self.hex_north_east, HexEdge.north_east),
            ]
            return self._neighbors

    @property
    def coords(self):
        return {
            'x': self.x,
            'y': self.y
        }

    def export(self):
        "Export Hex data as dict"
        data = self.map_data
        data['neighbors'] = {n[1].name: {'x': n[0].x, 'y': n[0].y } for n in self.neighbors}
        data['natural_resources'] = [r.name for r in self.natural_resources]
        return data
