from historia.utils import unique_id, random_country_colors
from historia.country.models.province import Province
from historia.log import LogAction

class Country(object):
    """
        Top level of government.
        Representation of a Country.
    """
    def __init__(self, manager, initial_hex, ancestor=None):
        super(self.__class__, self).__init__()
        self.manager = manager
        self.id = unique_id('co')

        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        # create a province
        capital = Province(self.manager, initial_hex, self, is_capital=True)
        self.provinces = [capital]
        self.capital = capital
        self.manager.logger.log(self, {
            'capital': capital.id
        })
        self.manager.logger.log(self, {
            'provinces': capital.id
        }, LogAction.extend)

        # Vassal countries under this country
        self.vassals = []
        self.is_vassal = False

        # tuple of Country, relation int
        self.relations = []

        map_color, border_color = random_country_colors()
        self.display = {
            'map_color': map_color.hex,
            'border_color': border_color.hex
        }

        self.name = ''

    def settle_hex(self, hex_inst):
        "Settles a new hex, creating a province and returning it"
        province = Province(self.manager, hex_inst, self, is_capital=False)
        self.provinces.append(province)
        return province

    @property
    def pops(self):
        pops = []
        for p in self.provinces:
            pops.extend(p.pops)
        return pops

    def __repr__(self):
        return "<Country: name={} id={}>".format(self.name, self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())


    def export(self):
        "Export country data"
        return {
            'display': self.display,
            'name': self.name,
            'provinces': [p.id for p in self.provinces]
        }
