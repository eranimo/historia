from enum import Enum

class Job(Enum):
    farmer = 'Farmer'
    hunter = 'Hunter'
    aristocrat = 'Aristocrat'
    soldier = 'Soldier'


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
        self.religion = religion
        self.language = language
        self.job = job
        self.savings = 0

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
