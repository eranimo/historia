from uuid import uuid4
from enum import Enum

from historia.enums.dict_enum import DictEnum
from historia.economy.enums.resource import Good


basic_needs = [
    (Good.fish, 0.5),
    (Good.fruit, 1.5),
    (Good.vegetable, 1.5),
    (Good.grain, 2.0)
]

class TestEnum(DictEnum):
    foo = { 'title': 'foo '}


class PopType(DictEnum):
    """
    title: the title of this Pop Type
    basic_needs: Good for staying alive
    daily_needs: Good that are not required for survival, but required to be productive
    luxury_needs: Good required in order to be happy

    rgo_worker: whether or not this pop type can work in an EGO

    """
    __defaults__ = {
        'rgo_worker': False,
        'rgo_owner': False
    }
    # farmers work in farm RGOs
    # get income from portion of RGO's income
    farmer = {
        'title': 'Farmer',
        'foo': [TestEnum.foo],
        'bar': TestEnum.foo,
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 2.5),
            (Good.alcohol, 5.0),
            (Good.clothes, 1.0)
        ],
        'rgo_worker': True
    }
    # Laborers work in mine RGOs
    # get income from portion of RGO's income
    laborer = {
        'title': 'Miner',
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 2.5),
            (Good.alcohol, 5.0),
            (Good.clothes, 1.0)
        ],
        'rgo_worker': True
    }
    # Craftsman produce goods from other goods
    # They do not work at RGOs, but instead earn an income by buying raw
    # materials to produce other goods
    craftsman = {
        'title': 'Craftsman',
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 5.0),
            (Good.alcohol, 3.0),
            (Good.clothes, 1.0)
        ]
    }
    # Aristocrats own RGOs
    # get income from sale of goods produced at owned RGOs
    aristocrat = {
        'title': 'Aristocrat',
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 5.0),
            (Good.alcohol, 5.0),
            (Good.clothes, 2.0),
            (Good.furnature, 0.1)
        ],
        'rgo_worker': True,
        'rgo_owner': True
    }
    # Soldiers are employed by the state, Soldiers don't work
    soldier = {
        'title': 'Soldier',
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 2.5),
            (Good.alcohol, 5.0),
            (Good.clothes, 1.0)
        ],
        'rgo_worker': True,
        'rgo_owner': True
    }

    # Merchants travel from one Market to another buying low and selling high
    # merchants look for Markets with goods that have a price lower than what they
    # cost in another province including travel cost and tariffs.
    merchant = {
        'title': 'Merchant',
        'basic_needs': basic_needs,
        'daily_needs': [
            (Good.tea, 4.0),
            (Good.alcohol, 4.0),
            (Good.clothes, 1.5),
            (Good.furnature, 0.1)
        ]
    }
    # TODO: add factoryworker, and officeworker pop types


promotion_tree = {
    PopType.farmer: {
        'promote': [
            PopType.craftsman
        ],
        'demote': [
            PopType.laborer
        ]
    },
    PopType.laborer: {
        'promote': [
            PopType.craftsman
        ],
        'demote': [
            PopType.farmer
        ]
    },
    PopType.craftsman: {
        'promote': [
            PopType.craftsman
        ],
        'demote': [
            PopType.farmer,
            PopType.laborer
        ]
    }
}
