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
        for x, row in enumerate(hexes):
            for y, h in enumerate(row):
                self.hexes.append(Hex(self, h))

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

    def export(self):
        hexes = [[None for y in range(self.size)] for x in range(self.size)]
        for h in self.hexes:
            hexes[h.x][h.y] = h.export()
        return hexes
