from historia.utils import unique_id
from historia.country.enums import PrimaryDivisionTypes, GovernmentType, GovernmentStructure
from historia.economy.models import Market
from historia.log import LogAction


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

        self.hex = location
        self.owner = owner
        self.hex.owner = self
        self.is_capital = is_capital

        # economy
        self.market = Market(self.manager, self)
        self.pops = []
        self.RGOs = []

        self.manager.logger.log(self, {
            'owner': owner.id
        })

    def add_pops(self, pops):
        "Add pops from a list."
        self.pops.extend(pops)
        self.manager.logger.log(self, {
            'pops': [p.id for p in pops]
        }, LogAction.extend)

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

    def export(self):
        return {
            'hex': self.hex.coords,
            'owner': self.owner.id,
            'pops': [],
            'rgos': []
        }
