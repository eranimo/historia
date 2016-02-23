from enum import Enum
from historia.enums.dict_enum import DictEnum

class PopClass(Enum):
    upper = 'Upper'
    middle = 'Middle'
    lower = 'Lower'

class PopType(DictEnum):
    """
    title: the title of this Pop Type
    promotes_to: a list of PopTypes that this pop can promote to when they are meeting their needs
        and space is available
    demotes_to: a list of PopTypes this pop can demote to if they aren't meeting their needs
    """
    # farmers work in fields and produce food goods
    farmer = {
        'title': 'Farmer',
        'promotes_to': [PopType.craftsman],
        'demotes_to': [PopType.hunter],
        'basic_needs': [

        ]
    }
    # Craftsman are skilled and produce manufactured goods
    craftsman = {
        'title': 'Craftsman'
    }
    # hunters produce food from forests and fields
    hunter = {
        'title': 'Hunter',
        'promotes_to': [PopType.craftsman],
        'demotes_to': [PopType.farmer]
    }
    # aristocrats own land and businesses
    aristocrat = {
        'title': 'Aristocrat',
        'promotes_to': [PopType.officer]
    }
    soldier = {
        'title': 'Soldier',
        'promotes_to': [PopType.officer]
    }
    officer = {
        'title': 'Officer'
    }

class Pop(object):
    """
    A simulated unit of population
    """

    def __init__(self, manager, culture, religion, language, job):
        """
        Creates a new Pop.
        manager  (Historia)
        culture  (Culture)
        religion (Religion)
        language (Language)
        job      (Job)
        """
        self.manager = manager

        self.culture = culture
        self.job = job
        self.savings = 0

        # the culture this pop is converting to
        self.culture_convert_to = None
        # which points this Pop has towards converting to this culture
        # when 100, this pop converts
        self.culture_convert_points = 0

    @property
    def income(self):
        """
        """
        pass

    def buy_needs(self):
        """
        """
        pass

    @property
    def happiness(self):
        """
        """
        pass

    @property
    def productivity(self):
        """
        """
        pass

    @property
    def militancy(self):
        """
        """
        pass
