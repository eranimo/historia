from uuid import uuid4

from historia.time import TimelineProperty
from historia.enums import PrimaryDivisionTypes, GovernmentType, GovernmentStructure

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



class PoliticalUnit(object):
    """
    Base class for Country, Primary and Secondary divisions
    """
    pass
    # def __init__(self):
    #     self.id = uuid4().hex
    #     self._name_timeline = []
    #     self._name = TimelineProperty(manager, self._name_timeline)
    #
    # @property
    # def name(self):
    #     return self._name.get(self.manager.current_day)
    #
    # @name.setter
    # def name(self, value):
    #     self._name.set(self.manager.current_day, value)
    #
    # def rename(self):
    #     """
    #     Randomly generates a new name
    #     """
    #     # TODO: import namegen to generate name
    #     # names should be based off climate
    #     pass


class PrimaryDivision(PoliticalUnit):
    """
    Short name: p-division.
    Middle level of government.
    Grouping of Counties.
    May be named something else under different government types.

    In Federal government organization, they have power.
    In Unitary government organization, they are ceremonial.

    Some provinces might be territories instead of true provinces.

    Counties in the province must be contigious, except islands.
    """

    def __init__(self, manager, initial, is_capital=False, province_type=None):
        super(self.__class__, self).__init__()
        self.manager = manager

        self.capital = capital # capital province?
        self.divisions = [initial]

        if province_type is None:
            self.province_type = PrimaryDivisionTypes.province
        elif type(province_type) is PrimaryDivisionTypes:
            self.province_type = province_type
        else:
            raise TypeError('province_type must be a PrimaryDivisionTypes enum')


class SecondaryDivision(PoliticalUnit):
    """
    Short name: s-division.
    Lowest level of government.
    May be named something else under different government types.
    Counties have:
        - population
    """

    def __init__(self, manager, location, is_capital):
        super(self.__class__, self).__init__()
        self.manager = manager

        self.hex = location
        self.hex.owner = self
        self.is_capital = is_capital

    @property
    def neighbors(self):
        """ Return neighboring counties """
        return [h.owner for h in self.hex.neighbors if h.owned]

    @property
    def is_border(self):
        """ Returns True if any county neighbors are owned land hexes """
        return any([h.owned for h in self.hex.neighbors if h.is_land])

    @property
    def is_frontier_county(self):
        """ Returns True if any hex neighbors are unowned land hexes """
        return any([not h.owned for h in self.hex.neighbors if h.is_land])

    def get_frontier_hexes(self):
        """ Gets the unowned land hexes neighboring this hex """
        return [h for h in self.hex.neighbors if h.is_land and not h.owned]

    @property
    def is_coastal(self):
        return self.hex.is_coast

    @property
    def has_river(self):
        return self.hex.has_river


class Country(PoliticalUnit):
    """
        Top level of government.
        Representation of a Country.
    """
    def __init__(self, manager, initial_hex, ancestor=None):
        super(self.__class__, self).__init__()
        self.manager = manager

        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        if initial_hex:
            # create a province
            second_level = SecondaryDivision(self.manager, initial_hex, is_capital=True)
            first_level = PrimaryDivision(self.manager, second_level, is_capital=True)
            self.divisions = [first_level]
        else:
            self.divisions = []

        # Vassal countries under this country
        self.vassals = []
        self.is_vassal = False

        # tuple of Country, relation int
        self.relations = []

    @property
    def num_counties(self):
        """ Number of Counties in this Country """
        return sum([len(p.divisions) for p in self.divisions])

    @property
    def counties(self):
        """ Returns a list of all counties """
        result = []
        for p in self.divisions:
            result.extend(p.divisions)
        return result

    @property
    def extinct(self):
        """ A country is extinct if it has no land """
        return len(self.divisions) == 0


    def reorganize(self):
        """
        Reorganize this countries primary divisions.
        Primary divisions should:
            ...be as equal in population as possible
            ...ideally be of the same biome
            ...ideally be separated by a river

        Algorithm:
            Flood fill around x points where x is target number of Primary divisions
            cost function:
                +1 = over same biome
                +3 = over different biome
                +5 = over river
        """
        target_province_size = 3
        ideal_num_primary_divisions = self.num_counties // target_province_size
        # TODO: implement

    def relations_with(self, other):
        """ Get the relations between this country and another """
        for country, relationship in self.relations:
            if country is other:
                return relationship
        raise 0
