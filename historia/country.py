class Province(object):
    """
    Middle level of government.
    Grouping of Counties.
    May be named something else under different government types.

    In Federal government organization, they have power.
    In Unitary government organization, they are ceremonial.

    Some provinces might be territories instead of true provinces.

    Counties in the province must be contigious, except islands.
    """

    def __init__(self):
        pass


class Country(object):
    """
    Lowest level of government.
    May be named something else under different government types.
    Counties have:
        - population
    """

    def __init__(self):
        pass


class Country(object):
    """
        Representation of a Country. Top level government division.
    """
    def __init__(self, manager, ancestor=None, initial_hex=None):
        self.manager = manager

        self._name_timeline = []
        self._name = TimelineProperty(self.manager, self._name_timeline)


        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        if initial_hex:
            # create a province
            self.territory = [initial_hex]
        else:
            self.territory = []

        # Vassal countries under this country
        self.vassals = []
        self.is_vassal = False

        # tuple of Country, relation int
        self.relations = []

    def reorganize(self):
        """
        Reorganize this countries provinces.
        Provinces should be as equal in population as possible.
        """
        pass

    def relations_with(self, other):
        """ Get the relations between this country and another """
        for country, relationship in self.relations:
            if country is other:
                return relationship
        raise 0

    @property
    def name(self):
        return self._name.get(self.manager.current_day)

    @name.setter
    def name(self, value):
        self._name.set(self.manager.current_day, value)
