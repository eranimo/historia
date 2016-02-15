from uuid import uuid4
import random
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

def find_spouse(me, people):
    """
    Finds a potential spouse in a list of people.
    Requirements:
    - Must be opposite gender
    - Must be fertile

    Spouse points:
    -10 for each year difference
    +100 for same religion
    +110 for same culture
    """
    # TODO: rich people should get higher spouse points
    # TODO: take Relation into account
    # TODO: arranged marriages
    if me.gender is Gender.male:
        match_gender = Gender.female
    else:
        match_gender = Gender.male
    eligible_people = [p for p in people if p.gender is match_gender and p.fertility > 0]

    ranked = []
    for p in eligible_people:
        points = 0
        if p.age > me.age:
            points -= (p.age - me.age) * 10
        if p.religion is me.religion:
            points += 100
        if p.culture is me.culture:
            points += 100
        ranked.append((p, points))
    ranked.sort(key=lambda tup: tup[1])
    if len(ranked) == 0:
        return None
    return ranked[-1][0]


class Person(object):
    def __init__(self, manager):
        self.manager = manager
        self.id = uuid4().hex

        self.mother = None
        self.father = None
        self.children = set()

        self._age = 0 # initial age
        self.birth_date = self.manager.current_day

        self.gender = random.choice([Gender.male, Gender.female])
        self.next_sex = None

        # pregnancy
        self.is_pregnant = False
        self.baby_due_date = None

        self.citizenship = None # Country

        # marriage
        self.is_married = False
        self.is_engaged = False
        self.spouse = None
        self.marriage_date = None
        self.engaged_to = None

        # social systems
        self.culture = None # CultureVariant
        self.language = None # LanguageVariant
        self.religion = None # ReligionVariant

    @classmethod
    def new_adult(cls, manager):
        """ Create an adult """
        person = Person(manager)
        person._age = random.randint(25, 35)
        return person

    @classmethod
    def born(cls, manager, mother, father):
        person = Person(manager)
        person.mother = mother
        person.father = father
        return person

    def death_chance(self):
        """ the chance that this person has of dying every day """
        return None

    @property
    def is_marriage_age(self):
        # TODO: marriage age should change with country, religion, culture
        return self.age > 15

    @property
    def is_adult(self):
        return self.age > 18

    @property
    def can_get_married(self):
        if self.is_married or self.is_engaged:
            return False
        if self.is_marriage_age:
            return True
        return False

    def get_engaged(self, other):
        if type(other) is not Person:
            raise Exception("`other` must be a Person")
        # TODO: implement a better way to find engagement day
        days = random.randint(1, 100)
        self.marriage_date = self.manager.current_day.replace(days=days)
        self.engaged_to = other
        self.is_engaged = True
        other.is_engaged = True
        other.engaged_to = self

    def break_engagement(self):
        # TODO: use this
        self.is_engaged = False
        self.engaged_to = None
        pass

    def check_marriage(self):
        return self.is_engaged is True and self.manager.current_day == self.marriage_date

    def get_married(self):
        if self.is_engaged is True:
            self.spouse = self.engaged_to
            self.marriage_date = None
            self.is_married = True
            self.is_engaged = False
            self.spouse.is_married = True
            self.spouse.is_engaged = False
            self.spouse.spouse = self
            self.have_sex(self.spouse)
            self.engaged_to = None
        else:
            raise Exception('Not engaged to anyone')

    @property
    def fertility(self):
        """
        Fertility is a value between 0 and 100
        Its the likelyhood of having a child. Both potential parents verility is averaged
        together. That number is the likelyhood of conception.
        A value of 0 means they are infertile
        """
        if self.age <= 12: # children can't have kids
            return 0
        # TODO: implement base fertility and fertility modifiers
        # TODO: implement contraception
        return 0.0001
        if self.age > 50 and self.gender is Gender.female:
            return 0
        if self.age > 50:
            return 0.001
        if self.age > 40:
            return 0.005
        if self.age > 25:
            return 0.01
        return 0.2

    def can_get_pregnant(self):
        if self.gender is Gender.female and self.is_pregnant is False:
            return True
        return False

    def have_sex(self, other):
        """
        Have sex with another Person.
        Return True if pregnant, False otherwise.
        """
        # TODO: having sex should increase relations with spouse
        # TODO: rape should do something. Traits maybe?
        # chance to have a baby

        # plan for next sex
        in_days = random.randint(5, 15)
        self.next_sex = self.manager.current_day.replace(days=+in_days)

        if type(other) is not Person:
            raise Exception("`other` must be a Person. Given: {}".format(other))
        if self.gender is Gender.female and self.is_pregnant or \
           self.gender is Gender.male and self.spouse.is_pregnant:
            return False
        total_fertility = (self.fertility + other.fertility) / 2.
        if total_fertility < (random.randint(0, 100) / 100.):
            # baby!
            if self.gender is Gender.male:
                other.get_pregnant(self)
            else:
                self.get_pregnant(other)
            return True
        return False

    def get_pregnant(self, partner):
        if self.gender is Gender.male:
            raise GenderError('Only females can get pregnant!')
        if self.is_pregnant is True:
            raise Exception('Already pregnant! {}'.format(self))
        self.is_pregnant = True
        self.baby_father = partner
        self.baby_due_date = self.manager.current_day.replace(months=+9)

    def check_pregnancy(self):
        return self.is_pregnant is True and self.manager.current_day == self.baby_due_date

    def have_baby(self):
        """ Females only """
        if self.is_pregnant is False:
            raise Exception('Not pregnant')
        if self.manager.current_day == self.baby_due_date:
            baby = Person.born(self.manager, self, self.baby_father)
            self.children.add(baby)
            self.baby_father.children.add(baby)

            self.is_pregnant = False
            self.baby_due_date = None
            self.baby_father = None

            # plan for next sex
            if self.baby_father is self.spouse:
                in_days = random.randint(3, 5)
                self.spouse.next_sex = self.manager.current_day.replace(days=+in_days)

            return baby
        raise Exception('Can\'t have baby yet: {}'.format(self))

    @property
    def age(self):
        """ Returns this persons age in years """
        return self._age + int(round((self.manager.current_day - self.birth_date).days / 365.))

    def __repr__(self):
        return "<Person age={} gender={} pregnant={}>".format(self.age, self.gender, self.is_pregnant)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())

    @property
    def stats(self):
        return {
            'gender': self.gender,
            'age': self.age,
            'is_married': self.is_married,
            'is_pregnant': self.is_pregnant,
            'spouse': self.spouse,
            'num_children': len(self.children),
            'fertility': self.fertility
        }
