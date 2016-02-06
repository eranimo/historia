from uuid import uuid4

from historia.enums.country_enums import ProvinceTypes


class PoliticalUnit(object):
    """
    Base class for Country, Province, County
    """
    def __init__(self):
        self.id = uuid4().hex
        self._name_timeline = []
        self._name = TimelineProperty(self.manager, self._name_timeline)

    @property
    def name(self):
        return self._name.get(self.manager.current_day)

    @name.setter
    def name(self, value):
        self._name.set(self.manager.current_day, value)

    def rename(self):
        """
        Randomly generates a new name
        """
        # TODO: import namegen to generate name
        # names should be based off climate
        pass


class Province(PoliticalUnit):
    """
    Middle level of government.
    Grouping of Counties.
    May be named something else under different government types.

    In Federal government organization, they have power.
    In Unitary government organization, they are ceremonial.

    Some provinces might be territories instead of true provinces.

    Counties in the province must be contigious, except islands.
    """

    def __init__(self, initial_county, is_capital=False, province_type=None):
        super(self.__class__, self).__init__()

        self.capital = capital # capital province?
        self.counties = [initial_county]

        if province_type is None:
            self.province_type = ProvinceTypes.province
        else if type(province_type) is ProvinceTypes:
            self.province_type = province_type
        else:
            raise TypeError('province_type must be a ProvinceTypes enum')


class County(PoliticalUnit):
    """
    Lowest level of government.
    May be named something else under different government types.
    Counties have:
        - population
    """

    def __init__(self, location, is_capital):
        super(self.__class__, self).__init__()

        self.hex = location
        self.hex.county = self
        self.is_capital = is_capital

    @property
    def neighbors(self):
        """ Return neighboring counties """
        return [h.county for h in self.hex.neighbors if h.owned]

    @property
    def is_border_county(self):
        """ Returns True if any county neighbors are owned land hexes """
        return any([h.owned for h in self.hex.neighbors if h.is_land])

    def get_frontier_hexes(self):
        """ Gets the unowned land hexes neighboring this hex """
        return [h for h in self.hex.neighbors if h.is_land and not h.owned]

    @property
    def is_frontier_county(self):
        """ Returns True if any hex neighbors are unowned land hexes """
        return any([not h.owned for h in self.hex.neighbors if h.is_land])

    @property
    def is_coastal(self):
        return self.hex.is_coast

    @property
    def has_river(self):
        return self.hex.has_river


class Country(PoliticalUnit):
    """
        Representation of a Country. Top level government division.
    """
    def __init__(self, manager, ancestor=None, initial_hex=None):
        super(self.__class__, self).__init__()

        self.manager = manager

        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        if initial_hex:
            # create a province
            first_county = County(initial_hex, is_capital=True)
            first_province = Province(county=first_county, is_capital=True)
            self.provinces = [first_province]
        else:
            self.provinces = []

        # Vassal countries under this country
        self.vassals = []
        self.is_vassal = False

        # tuple of Country, relation int
        self.relations = []

    @property
    def num_counties(self):
        """ Number of Counties in this Country """
        return sum([len(p.counties) for p in self.provinces])

    @property
    def counties(self):
        """ Returns a list of all counties """
        result = []
        for p in self.provinces:
            result.extend(p.counties)
        return result

    @property
    def extinct(self):
        """ A country is extinct if it has no land """
        return len(self.provinces) == 0


    def reorganize(self):
        """
        Reorganize this countries provinces.
        Provinces should be as equal in population as possible.
        """
        target_province_size = 3
        ideal_num_provinces = self.num_counties // target_province_size
        # TODO: implement

    def relations_with(self, other):
        """ Get the relations between this country and another """
        for country, relationship in self.relations:
            if country is other:
                return relationship
        raise 0
