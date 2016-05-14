from uuid import uuid4
from enum import Enum

from historia.enums.dict_enum import DictEnum
from historia.economy.enums.resource import Good
from historia.pops import logic
from historia.pops.enums.pop_class import PopClass


class PopJob(DictEnum):
    "Role that each Pop plays in the economic simulation"
    __exports__ = ['title', 'color']

    # bread, lumber, tools -> grain
    farmer = {
        'title': 'Farmer',
        'color': 'green',
        'logic': logic.farmer,
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.proletariat,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.proletariat,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.proletariat,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.proletariat,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.bourgeoisie,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.proletariat,
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
        'inventory_size': 150,
        'start_money': 10,
        'social_class': PopClass.bourgeoisie,
        'start_inventory': [
            {'good': Good.grain, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.grain, 'amount': 5}
        ]
    }

    merchant = {
        'title': 'Merchant',
        'color': 'purple',
        'logic': logic.merchant,
        'inventory_size': 500,
        'start_money': 30,
        'social_class': PopClass.bourgeoisie,
        'start_inventory': [
            {'good': Good.bread, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.bread, 'amount': 3}
        ]
    }

JOBS_CLASS = {
    PopClass.aristocracy: [],
    PopClass.bourgeoisie: [
        PopJob.blacksmith,
        PopJob.baker,
        PopJob.merchant
    ],
    PopClass.proletariat: [
        PopJob.farmer,
        PopJob.miner,
        PopJob.miller,
        PopJob.woodcutter,
        PopJob.refiner
    ]
}
