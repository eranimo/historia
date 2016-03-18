from uuid import uuid4

from historia.country.models.province import Province

class Country(object):
    """
        Top level of government.
        Representation of a Country.
    """
    def __init__(self, manager, initial_hex=None, ancestor=None):
        super(self.__class__, self).__init__()
        self.manager = manager
        self.id = uuid4().hex

        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        if initial_hex:
            # create a province
            self.provinces = [Province(self.manager, initial_hex, is_capital=True)]
        else:
            self.provinces = []

        # Vassal countries under this country
        self.vassals = []
        self.is_vassal = False

        # tuple of Country, relation int
        self.relations = []

    def __repr__(self):
        return "<Country: id={}>".format(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())
