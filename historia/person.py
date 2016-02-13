from enum import Enum

class Gender(Enum):
    male = 'Male'
    female = 'Female'
    # sorry

class Job(Enum):
    soldier = 'Soldier' # educated
    warrior = 'Warrior' # uneducated
    farmer = 'Farmer'
    fisherman = 'Fisherman'
    hunter = 'Hunter'
    gatherer = 'Gatherer'

class GenderError(Exception):
    pass


class Person(object):
    def __init__(self, manager):
        self.manager = manager
        self.job = None

        self.birth_date = self.manager.current_day

        self.gender = None

        # pregnancy
        self.is_pregnant = False
        self.baby_due_date = None

        self.citizenship = None # Country

        # social systems
        self.culture = None # CultureVariant
        self.language = None # LanguageVariant
        self.religion = None # ReligionVariant

    def death_chance(self):
        """ the chance that this person has of dying every day """
        return None

    @property
    def fertility(self):
        """
        Fertility is a value between 0 and 100.
        """

    def get_pregnant(self):
        if slef.gender is Gender.male:
            raise GenderError('Only females can get pregnant')
        self.is_pregnant = True
        self.baby_due_date = self.manager.current_day.replace(months=+8)

    def have_baby(self):
        if self.manager.current_day == self.baby_due_date:
            baby = Person(self.manager)
            return baby
        raise Exception('Can\t have baby yet')

    @property
    def age(self):
        return (self.manager.current_day - self.birth_date).year
