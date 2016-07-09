import random

from historia.hex import Hex

class HexNotFoundException(Exception):
    pass

class WorldMap:
    """
        Representation of the map Historia is running on
    """
    def __init__(self, map_data):
        self.details = map_data.get('details')
        self.size = self.details.get('size')

        self.hexes = []
        hexes = map_data.get('hexes')
        self.hex_map = [[None for y in range(self.size)] for x in range(self.size)]
        for x, row in enumerate(hexes):
            for y, h in enumerate(row):
                hex_inst = Hex(self, h)
                self.hex_map[x][y] = hex_inst
                self.hexes.append(hex_inst)

    @property
    def unowned_hexes(self):
        return [h for h in self.hexes if h.owner is None]

    def find_hex(self, x, y):
        for h in self.hexes:
            if h.x == x and h.y == y:
                return h
        raise HexNotFoundException('Could not find hex at {}, {}'.format(x, y))

    def random_hex(self, type=None):
        found = random.choice(self.hexes)
        if type is not None:
            while found.type is type:
                found = random.choice(self.hexes)
        return found

    def get_map_mode(self, map_mode):
        return [[h.reference(map_mode) for h in row] for row in self.hex_map]
