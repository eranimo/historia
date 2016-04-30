from historia.utils import unique_id
from historia.country.enums import PrimaryDivisionTypes, GovernmentType, GovernmentStructure
from historia.economy.models import Market
from historia.namegen import random_word


class Province(object):
    """
    Subdivision of government.
    Provinces have:
        - population
    """

    def __init__(self, manager, location, owner, is_capital=False):
        super(self.__class__, self).__init__()
        self.manager = manager
        self.id = unique_id('pr')

        self.name = random_word()

        self.hex = location
        self.hex.owner = self
        self.owner = owner
        self.is_capital = is_capital

        self.date_founded = self.manager.current_day

        # economy
        self.market = Market(self.manager, self)
        self.pops = []
        self.RGOs = []


    def __repr__(self):
        return "<Province id={} owner={}>".format(self.id, self.owner)

    def add_pops(self, pops):
        "Add pops from a list."
        self.pops.extend(pops)

    @property
    def neighbors(self):
        """ Return neighboring provinces """
        return [h[0].owner for h in self.hex.neighbors if h[0].owner]

    @property
    def owned_neighbors(self):
        """ Return neighboring owned provinces """
        return [h[0].owner for h in self.hex.neighbors if h[0].owner and h[0].owner.owner is self.owner]

    @property
    def is_border(self):
        """ Returns True if any county neighbors are owner land hexes """
        return any([h[0].owner for h in self.hex.neighbors if h[0].is_land])

    @property
    def is_frontier(self):
        """ Returns True if any hex neighbors are unowner land hexes """
        return any([not h[0].owner for h in self.hex.neighbors if h[0].is_land])

    def get_frontier_hexes(self):
        """ Gets the unowner land hexes neighboring this hex """
        return [h[0] for h in self.hex.neighbors if h[0].is_land and h[0].owner is None]

    @property
    def is_coastal(self):
        return self.hex.is_coast

    @property
    def has_river(self):
        return self.hex.has_river

    def export(self):
        return {
            'hex': self.hex.coords,
            'name': self.name,
            'date_founded': self.date_founded.format("YYYY-MM-DD"),
            'owner': self.owner.id,
            'is_capital': self.is_capital,
            'market': self.market.export(),
            'pops': [p.id for p in self.pops]
        }
