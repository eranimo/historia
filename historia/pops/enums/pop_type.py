from uuid import uuid4
from enum import Enum

from historia.enums.dict_enum import DictEnum
from historia.economy.enums.resource import Good
from historia.pops import logic

# basic_needs = [
#     (Good.fish, 0.5),
#     (Good.fruit, 1.5),
#     (Good.vegetable, 1.5),
#     (Good.grain, 2.0)
# ]


class PopType(DictEnum):
    """
    title: the title of this Pop Type

    """
    # __defaults__ = {
    #     'rgo_worker': False,
    #     'rgo_owner': False,
    #     'basic_needs': basic_needs
    # }
    __exports__ = ['title', 'color']

    # bread, lumber, tools -> grain
    farmer = {
        'title': 'Farmer',
        'color': 'green',
        'logic': logic.farmer,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.timber, 'amount': 1},
            {'good': Good.tools, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.timber, 'amount': 3},
            {'good': Good.tools, 'amount': 1}
        ]
    }

    # bread, tools -> iron_ore
    miner = {
        'title': 'Miner',
        'color': 'gray',
        'logic': logic.miner,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.tools, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.tools, 'amount': 1}
        ]
    }

    # bread, tools, timber -> lumber
    miller = {
        'title': 'Miller',
        'color': 'yellow',
        'logic': logic.miller,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.timber, 'amount': 1},
            {'good': Good.tools, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.timber, 'amount': 3},
            {'good': Good.tools, 'amount': 1}
        ]
    }

    # bread, tools -> timber
    woodcutter = {
        'title': 'Woodcutter',
        'color': 'brown',
        'logic': logic.woodcutter,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.tools, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.tools, 'amount': 1}
        ]
    }

    # bread, iron, lumber -> tools
    blacksmith = {
        'title': 'Blacksmith',
        'color': 'black',
        'logic': logic.blacksmith,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.iron, 'amount': 1},
            {'good': Good.lumber, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.iron, 'amount': 3},
            {'good': Good.lumber, 'amount': 3}
        ]
    }

    # bread, iron_ore, tools -> iron
    refiner = {
        'title': 'Refiner',
        'color': 'red',
        'logic': logic.refiner,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1},
            {'good': Good.iron_ore, 'amount': 1},
            {'good': Good.tools, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3},
            {'good': Good.iron_ore, 'amount': 5},
            {'good': Good.tools, 'amount': 1}
        ]
    }

    # grain -> bread
    baker = {
        'title': 'Baker',
        'color': 'orange',
        'logic': logic.baker,
        'start_inventory': [
            {'good': Good.grain, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.grain, 'amount': 5}
        ]
    }

    # # Craftsman produce goods from other goods
    # # They do not work at RGOs, but instead earn an income by buying raw
    # # materials to produce other goods
    # craftsman = {
    #     'title': 'Craftsman',
    #     'basic_needs': basic_needs,
    #     'daily_needs': [
    #         (Good.tea, 5.0),
    #         (Good.alcohol, 3.0),
    #         (Good.clothes, 1.0)
    #     ]
    # }
    # # Aristocrats own RGOs
    # # get income from sale of goods produced at owned RGOs
    # aristocrat = {
    #     'title': 'Aristocrat',
    #     'basic_needs': basic_needs,
    #     'daily_needs': [
    #         (Good.tea, 5.0),
    #         (Good.alcohol, 5.0),
    #         (Good.clothes, 2.0),
    #         (Good.furnature, 0.1)
    #     ],
    #     'rgo_worker': True,
    #     'rgo_owner': True
    # }
    # # Soldiers are employed by the state, Soldiers don't work
    # soldier = {
    #     'title': 'Soldier',
    #     'basic_needs': basic_needs,
    #     'daily_needs': [
    #         (Good.tea, 2.5),
    #         (Good.alcohol, 5.0),
    #         (Good.clothes, 1.0)
    #     ],
    #     'rgo_worker': True,
    #     'rgo_owner': True
    # }
    #
    # # Merchants travel from one Market to another buying low and selling high
    # # merchants look for Markets with goods that have a price lower than what they
    # # cost in another province including travel cost and tariffs.
    # merchant = {
    #     'title': 'Merchant',
    #     'basic_needs': basic_needs,
    #     'daily_needs': [
    #         (Good.tea, 4.0),
    #         (Good.alcohol, 4.0),
    #         (Good.clothes, 1.5),
    #         (Good.furnature, 0.1)
    #     ]
    # }
    # # TODO: add factoryworker, and officeworker pop types


# promotion_tree = {
#     PopType.farmer: {
#         'promote': [
#             PopType.craftsman
#         ],
#         'demote': [
#             PopType.laborer
#         ]
#     },
#     PopType.laborer: {
#         'promote': [
#             PopType.craftsman
#         ],
#         'demote': [
#             PopType.farmer
#         ]
#     },
#     PopType.craftsman: {
#         'promote': [
#             PopType.craftsman
#         ],
#         'demote': [
#             PopType.farmer,
#             PopType.laborer
#         ]
#     }
# }


if __name__ == "__main__":
    e = PopType.export_all()
    print(e)
