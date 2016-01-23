from historia.gen import Historia
from historia.map import WorldMap
from historia.hex import Hex


edges = {
    'east': {'is_river': False, 'is_coast': False},
    'north_east': {'is_river': False, 'is_coast': False},
    'north_west': {'is_river': False, 'is_coast': False},
    'west': {'is_river': False, 'is_coast': False},
    'south_west': {'is_river': False, 'is_coast': False},
    'south_east': {'is_river': False, 'is_coast': False},
}
mock_map_data = {
    'details': {
        'size': 3
    },
    # 4 5 4
    #  3 5 3
    # 2 6 3

    'hexes': [
        [
            { 'x': 0, 'y': 0, 'altitude': 4, 'edges': edges },
            { 'x': 0, 'y': 1, 'altitude': 5, 'edges': edges },
            { 'x': 0, 'y': 2, 'altitude': 4, 'edges': edges }
        ],
        [
            { 'x': 1, 'y': 0, 'altitude': 3, 'edges': edges },
            { 'x': 1, 'y': 1, 'altitude': 5, 'edges': edges },
            { 'x': 1, 'y': 2, 'altitude': 3, 'edges': edges }
        ],
        [
            { 'x': 2, 'y': 0, 'altitude': 2, 'edges': edges },
            { 'x': 2, 'y': 1, 'altitude': 6, 'edges': edges },
            { 'x': 2, 'y': 2, 'altitude': 3, 'edges': edges }
        ]
    ]
}
mock_map = WorldMap(mock_map_data)

mock_manager = Historia(mock_map_data)
