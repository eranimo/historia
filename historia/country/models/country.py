import random
from historia.utils import unique_id, random_country_colors
from historia.country.models.province import Province
from historia.log import LogAction
from historia.pops import make_initial_pops
from historia.namegen import random_word
from historia.world import give_hex_natural_resources

class Country(object):
    """
        Top level of government.
        Representation of a Country.
    """
    def __init__(self, manager, initial_hex, ancestor=None):
        super(self.__class__, self).__init__()
        self.manager = manager
        self.id = unique_id('co')

        self.name = random_word()

        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

        # hexes this country controls
        # create a province
        capital = Province(self.manager, initial_hex, self, is_capital=True)
        self.provinces = [capital]
        self.capital = capital

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

        self.group_provinces = []

    def settle_hex(self, hex_inst):
        "Settles a new hex, creating a province and returning it"
        province = Province(self.manager, hex_inst, self, is_capital=False)
        self.add_province(province)
        return province

    def add_province(self, province):
        "Add a province to this country"
        self.provinces.append(province)
        self.detect_groups()

    def settle_frontier(self):
        "Settle a random unowned frontier hex"
        frontier_provinces = [p for p in self.provinces if p.is_frontier]
        selected = random.choice(frontier_provinces)
        new_hex = selected.get_frontier_hexes()[0]
        give_hex_natural_resources(new_hex)
        new_province = self.settle_hex(new_hex)
        pops = make_initial_pops(new_province)
        new_province.add_pops(pops)
        print('added ', new_province)

        self.manager.stores['Province'].add(new_province)
        self.manager.stores['Pop'].add(pops)

    @property
    def pops(self):
        "Get all Pops in all of the Provinces in this country"
        pops = []
        for p in self.provinces:
            pops.extend(p.pops)
        return pops

    def detect_groups(self):
        "Detects and categorizes contiguous groupings of provinces, returning their midpoints"
        current_province = self.provinces[0]
        groups = [self.provinces]

        # provinces = set(self.provinces)
        #
        #
        # # compile list of province groups
        # while len(provinces) > 0:
        #     neighbors = [p for p in current_province.owned_neighbors if p in provinces]
        #     if len(neighbors) > 0:
        #         provinces.remove(current_province)
        #         current_province = neighbors[0]
        #         groups[-1].append(current_province)
        #     else:
        #         # start a new group
        #         new_prov = provinces.pop()
        #         current_province = new_prov
        #         groups[-1].append(current_province)
        #         # groups.append([new_prov])
        #

        coordinates = []

        # convert list of province groups into coordinate list
        for g in groups:
            x = 0
            y = 0
            for p in g:
                x += p.hex.x
                y += p.hex.y

            x /= len(g)
            y /= len(g)
            coordinates.append({ 'x_coord': x, 'y_coord': y })

        self.group_provinces = coordinates


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
            'groups': self.group_provinces,
            'provinces': [p.id for p in self.provinces]
        }
