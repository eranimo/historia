from historia.enums.dict_enum import DictEnum


class PopClass(DictEnum):
    "Social standing of each Pop"
    __exports__ = ['title', 'color']

    aristocracy = {
        'title': 'Aristocracy',
        'color': 'purple'
    }
    bourgeoisie = {
        'title': 'Bourgeoisie',
        'color': 'blue'
    }
    proletariat = {
        'title': 'proletariat',
        'color': 'red'
    }
