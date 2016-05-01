from historia.enums.dict_enum import DictEnum


class PopClass(DictEnum):
    "Social standing of each Pop"
    __exports__ = ['title', 'color']

    # Live off rent and taxes
    # live in cities
    aristocracy = {
        'title': 'Aristocracy',
        'color': 'purple'
    }

    # Trades goods and turns goods into other goods
    # live in cities and towns
    bourgeoisie = {
        'title': 'Bourgeoisie',
        'color': 'blue'
    }

    # Produces raw goods
    # live in rural areas
    proletariat = {
        'title': 'proletariat',
        'color': 'red'
    }
