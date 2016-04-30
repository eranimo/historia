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
        'social_class': PopClass.proletariat,
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
        'social_class': PopClass.proletariat,
        'start_inventory': [
            {'good': Good.grain, 'amount': 1}
        ],
        'ideal_inventory': [
            {'good': Good.grain, 'amount': 5}
        ]
    }
