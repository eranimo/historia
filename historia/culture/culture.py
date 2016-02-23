from uuid import uuid4

class Culture(object):
    """
    Culture.

    Considerations that go into making up a Culture:
    - language
    - history
    - food
    - shelter
    - education
    - security
    - relationships
    - political and social organizations
    - religions
    - art

    e.g. Chinese
    """

    def __init__(self, manager, name, parent=None):
        self.manager = manager
        self.id = uuid4().hex
        self.name = name

        # regional variations of this culture
        self.variants = []

        # descendant cultures
        self.children = []

        # which culture this culture branched off of
        # if None, this culture existed at simulation start
        self.parent = parent

        # a measure of how successful this culture is
        # a higher prestige means Pops are more likely to assimilate to this culture
        self.prestige = 0

    def recalculate_prestige(self):
        """
        Calculate the prestige of this culture
        1 for each pop of this culture
        100 for each country where this culture is dominant
        1/10th of each country's score where this culture is dominant
        """
        self.prestige = 0

    def split(self):
        """
        Create a new culture descended from this one
        """
        new_culture = Culture(self.manager, )
        self.children.append(new_culture)
        return new_culture

    def __repr__(self):
        raise "<Culture id={}>".format(self.system_name, self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())
