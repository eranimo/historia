from enum import Enum

from historia.enums.dict_enum import DictEnum

# TODO: rename to Good
class Resource(DictEnum):

    # Raw
    grain = { 'title': 'Grain' }
    fish = { 'title': 'Fish' }
    fruit = { 'title': 'Fruit' }
    vegetable = { 'title': 'Vegetable' }
    iron = { 'title': 'Iron' }
    timber = { 'title': 'Timber' }
    tea = { 'title': 'Tea' }
    wool = { 'title': 'Wool' }
    cotton = { 'title': 'Cotton' }

    # Produced
    bread = { 'title': 'Bread' }
    alcohol = { 'title': 'Alcohol' }
    lumber = { 'title': 'Lumber' }
    clothes = { 'title': 'Clothes' }
    fabric = { 'title': 'Fabric' }
    furnature = { 'title': 'Furnature' }


class NaturalResource(Enum):
    iron
    fish
    cotton
    timber

class PlantedResources(Enum):
    grains = {'good': Good.grain}
    fruit = {'good': Good.fruit}
    vegetable = {'good': Good.vegetable}
    tea_plant = {'good': Good.tea}
    sheep = {'good': Good.wool}
    cotton_plant = {'good': Good.cotton}


# production tree for producing Resource
# for input, 1st level list items are ALL,
#            2nd level list items are OR
production_tree = {
    Resource.bread: {
        'input': [
            (Resource.grain, 2)
        ],
        'output': 2
    },
    Resource.lumber: {
        'input': [
            (Resource.timber, 100)
        ],
        'output': 100
    },
    Resource.alcohol: {
        'input': [
            [
                (Resource.grain, 100),
                (Resource.fruit, 100)
            ]
        ],
        'output': 10
    },
    Resource.fabric: {
        'input': [
            (Resource.cotton, 10)
        ],
        'output': 5
    },
    Resource.clothes: {
        'input': [
            (Resource.fabric, 10),
        ],
        'output': 5
    },
    Resource.furnature: {
        'input': [
            (Resource.lumber, 10),
        ],
        'output': 1
    }
}

# TODO: implement the following Resource
# - jackets (wool)
# - luxury clothes (silk, wool, clothes)
