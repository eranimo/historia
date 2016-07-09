from historia.enums.dict_enum import DictEnum

class Biome(DictEnum):
    __exports__ = ['title', 'color', 'id']
    arctic = {
        'id': 1,
        'title': 'Arctic',
        'color': (224, 224, 224),
        'fertility': 1,
        'can_farm': False,
        'has_forest': False,
        'base_favorability': 10
    }
    tundra = {
        'id': 2,
        'title': 'Tundra',
        'color': (114, 153, 128),
        'fertility': 15,
        'can_farm': False,
        'has_forest': False,
        'base_favorability': -30
    }
    alpine_tundra = {
        'id': 3,
        'title': 'Alpine Tundra',
        'color': (97, 130, 106),
        'fertility': 10,
        'can_farm': False,
        'has_forest': False,
        'base_favorability': -20
    }
    desert = {
        'id': 4,
        'title': 'Desert',
        'color': (237, 217, 135),
        'fertility': 5,
        'can_farm': False,
        'has_forest': False,
        'base_favorability': -10
    }
    shrubland = {
        'id': 5,
        'title': 'Shrubland',
        'color': (194, 210, 136),
        'fertility': 20,
        'can_farm': True,
        'has_forest': False,
        'base_favorability': 20
    }
    savanna = {
        'id': 6,
        'title': 'Savanna',
        'color': (219, 230, 158),
        'fertility': 80,
        'can_farm': True,
        'has_forest': False,
        'base_favorability': 30
    }
    grasslands = {
        'id': 7,
        'title': 'Grasslands',
        'color': (166, 223, 106),
        'fertility': 150,
        'can_farm': True,
        'has_forest': False,
        'base_favorability': 50
    }
    boreal_forest = {
        'id': 8,
        'title': 'Boreal Forest',
        'color': (28, 94, 74),
        'fertility': 30,
        'can_farm': True,
        'has_forest': True,
        'base_favorability': -10
    }
    temperate_forest = {
        'id': 9,
        'title': 'Temperate Forest',
        'color': (76, 192, 0),
        'fertility': 100,
        'can_farm': True,
        'has_forest': True,
        'base_favorability': 50
    }
    temperate_rainforest = {
        'id': 10,
        'title': 'Temperate Rainforest',
        'color': (89, 129, 89),
        'fertility': 100,
        'can_farm': True,
        'has_forest': True,
        'base_favorability': -10
    }
    tropical_forest = {
        'id': 11,
        'title': 'Tropical Forest',
        'color': (96, 122, 34),
        'fertility': 70,
        'can_farm': True,
        'has_forest': True,
        'base_favorability': 5
    }
    tropical_rainforest = {
        'id': 12,
        'title': 'Tropical Rainforest',
        'color': (0, 70, 0),
        'fertility': 60,
        'can_farm': True,
        'has_forest': True,
        'base_favorability': 0
    }
