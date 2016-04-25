from historia.gen import Historia
from historia.map import WorldMap
from historia.hex import Hex
from historia.world import Biome
from historia.country import Country
from historia.pops import Pop

edges = {
    'east': {'is_river': False, 'is_coast': False},
    'north_east': {'is_river': False, 'is_coast': False},
    'north_west': {'is_river': False, 'is_coast': False},
    'west': {'is_river': False, 'is_coast': False},
    'south_west': {'is_river': False, 'is_coast': False},
    'south_east': {'is_river': False, 'is_coast': False},
}

def random_biome():
    biome = Biome.random()
    return { 'name': biome.name }

mock_map_data = {
    'details': {
        'size': 3,
        'sea_level': 4
    },
    # 4 5 4
    #  3 5 3
    # 2 6 3

    'hexes': [
        [
            { 'x': 0, 'y': 0, 'altitude': 4, 'edges': edges, 'biome': random_biome() },
            { 'x': 0, 'y': 1, 'altitude': 5, 'edges': edges, 'biome': random_biome() },
            { 'x': 0, 'y': 2, 'altitude': 4, 'edges': edges, 'biome': random_biome() }
        ],
        [
            { 'x': 1, 'y': 0, 'altitude': 3, 'edges': edges, 'biome': random_biome() },
            { 'x': 1, 'y': 1, 'altitude': 5, 'edges': edges, 'biome': random_biome() },
            { 'x': 1, 'y': 2, 'altitude': 3, 'edges': edges, 'biome': random_biome() }
        ],
        [
            { 'x': 2, 'y': 0, 'altitude': 2, 'edges': edges, 'biome': random_biome() },
            { 'x': 2, 'y': 1, 'altitude': 6, 'edges': edges, 'biome': random_biome() },
            { 'x': 2, 'y': 2, 'altitude': 3, 'edges': edges, 'biome': random_biome() }
        ]
    ]
}
mock_map = WorldMap(mock_map_data)

mock_manager = Historia(mock_map_data)

def make_mock_country(manager, initial_hex):
    return Country(manager, initial_hex)

def make_mock_pop(province, pop_type, population=10000):
    return Pop(province, pop_type, population)
