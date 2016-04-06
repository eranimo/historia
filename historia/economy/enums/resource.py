from enum import Enum

from historia.enums.dict_enum import DictEnum

class Good(DictEnum):
    "A physical commodity consumed by Pops"
    __exports__ = ['title']
    # Raw
    grain = { 'title': 'Grain' }
    meat = { 'title': 'Meat'}
    fish = { 'title': 'Fish' }
    fruit = { 'title': 'Fruit' }
    vegetable = { 'title': 'Vegetable' }
    iron_ore = { 'title': 'Iron Ore' }
    timber = { 'title': 'Timber' }
    tea = { 'title': 'Tea' }
    wool = { 'title': 'Wool' }
    cotton = { 'title': 'Cotton' }

    # Produced
    iron = { 'title': 'Iron' }
    tools = { 'title': 'Tools' }
    bread = { 'title': 'Bread' }
    alcohol = { 'title': 'Alcohol' }
    lumber = { 'title': 'Lumber' }
    clothes = { 'title': 'Clothes' }
    fabric = { 'title': 'Fabric' }
    furnature = { 'title': 'Furnature' }
    charcoal = { 'title': 'Charcoal' }


class NaturalResource(Enum):
    iron = {'good': Good.iron}
    fish = {'good': Good.fish}
    trees = {'good': Good.timber}

class PlantedResources(Enum):
    grains = {'good': Good.grain}
    fruit = {'good': Good.fruit}
    vegetable_plants = {'good': Good.vegetable}
    sheep = {'good': Good.wool}
    cattle = {'good': Good.meat}
    tea_plants = {'good': Good.tea}
    cotton_plants = {'good': Good.cotton}


# production tree for producing Good
# for input, 1st level list items are ALL,
#            2nd level list items are OR
# TODO: these need to be tweaked
production_tree = {
    Good.iron: {
        'input': [
            (Good.iron_ore, 1)
        ],
        'output': 1
    },
    Good.tools: {
        'input': [
            (Good.iron, 5)
        ],
        'output': 5
    },
    Good.bread: {
        'input': [
            (Good.grain, 2)
        ],
        'output': 2
    },
    Good.lumber: {
        'input': [
            (Good.timber, 100)
        ],
        'output': 100
    },
    Good.alcohol: {
        'input': [
            [
                (Good.grain, 100),
                (Good.fruit, 100)
            ]
        ],
        'output': 10
    },
    Good.fabric: {
        'input': [
            (Good.cotton, 10)
        ],
        'output': 5
    },
    Good.clothes: {
        'input': [
            (Good.fabric, 10),
        ],
        'output': 5
    },
    Good.furnature: {
        'input': [
            (Good.lumber, 10),
        ],
        'output': 1
    },
    Good.charcoal: {
        'input': [
            (Good.timber, 10),
        ],
        'output': 5
    }
}

# TODO: implement the following Good
# - jackets (wool)
# - luxury clothes (silk, wool, clothes)
