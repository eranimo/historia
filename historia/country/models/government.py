class Government(object):
    """
    This class represents the government of a country.
    """
    def __init__(self, manager, country):
        self.manager = manager
        self.country = country

        # GovernmentStructure
        self.organization = None

        # GovernmentTypes
        self.type = None

        # EthnicComposition
        self.composition = None

    @property
    def formal_name(self):
        if GovernmentType.republic:
            if GovernmentStructure.unitary:
                return 'Republic of %s' % (self.country.name)
            elif GovernmentStructure.federal:
                return 'Federal Republic of %s' % (self.country.name)
            elif GovernmentStructure.confederal:
                return 'Union of %s' % (self.country.name)
        elif GovernmentType.monarchy:
            if GovernmentStructure.unitary:
                return 'Kingdom of %s' % (self.country.name)
            else:
                return 'United Kingdom of %s' % (self.country.name)
        else:
            return 'State of %s' % (self.country.name)

    @property
    def description(self):
        """
            e.g. Japan: unitary parliamentary constitutional monarchy
            e.g. Saudi Arabia: unitary Islamic absolute monarchy
            e.g. Vatican City: ecclesiastical elective absolute theocratic monarchy
        """
        return ""
