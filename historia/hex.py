from historia.enums import HexEdge

class Hex:
    """
        Smallest unit on the map
        Horizontal hexagons
        Modified version from Hexgen
    """
    def __init__(self, world_map, data):
        self.world_map = world_map
        self.x = data.get('x')
        self.y = data.get('y')
        self.altitude = data.get('altitude')

        edges = data.get('edges')

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


    def __repr__(self):
        return "<Hex: x={} y={} altitude={}>".format(self.x, self.y, self.altitude)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    @property
    def hex_east(self):
        """ Returns the hex to the East or None if end of map"""
        if self.y == self.world_map.size:
            return self.world_map.find_hex(self.x, 0)
        else:
            return self.world_map.find_hex(self.x, self.y + 1)

    @property
    def hex_west(self):
        """ Returns the hex to the West or None if end of map"""
        if self.y == 0:
            return self.world_map.find_hex(self.x, self.world_map.size)
        else:
            return self.world_map.find_hex(self.x, self.y - 1)

    @property
    def hex_north_west(self):
        """ Returns the hex to the north west"""
        if self.x == 0:  # top of map
            return self.world_map.find_hex(0, round(self.y / -1 + self.world_map.size))
        elif self.y == 0 and self.x % 2 == 0:  # left of map and even
            return self.world_map.find_hex(self.x - 1, self.world_map.size)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x - 1, self.y - 1)
            else:
                return self.world_map.find_hex(self.x - 1, self.y)

    @property
    def hex_north_east(self):
        """ Returns the hex to the North East or None if end of map"""
        if self.x == 0:  # top of map
            return self.world_map.find_hex(0, round(self.y / -1 + self.world_map.size))
        elif self.y == self.world_map.size and self.x % 2 == 1:  # right of map and x is odd
            return self.world_map.find_hex(self.x - 1, 0)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x - 1, self.y)
            else:
                return self.world_map.find_hex(self.x - 1, self.y + 1)

    @property
    def hex_south_west(self):
        """ Returns the hex to the South West or None if end of map"""
        if self.x == self.world_map.size:  # bottom of map
            return self.world_map.find_hex(self.world_map.size, round(self.y / -1 + self.world_map.size))
        elif self.y == 0 and self.x % 2 == 1:  # left of map and x is odd
            return self.world_map.find_hex(self.x - 1, self.world_map.size)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x + 1, self.y - 1)
            else:
                return self.world_map.find_hex(self.x + 1, self.y)

    @property
    def hex_south_east(self):
        """ Returns the hex to the South East or None if end of map"""
        if self.x == self.world_map.size:  # bottom of map
            return self.world_map.find_hex(self.world_map.size, round(self.y / -1 + self.world_map.size))
        elif self.y == self.world_map.size and self.x % 2 == 1:  # right of map and x is odd
            return self.world_map.find_hex(self.x + 1, 0)
        else:
            if self.x % 2 == 0:  # even
                return self.world_map.find_hex(self.x + 1, self.y)
            else:
                return self.world_map.find_hex(self.x + 1, self.y + 1)

    @property
    def neighbors(self):
        """ Surrounding hexes with HexEdge enums """
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
