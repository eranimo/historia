import random, time, arrow, json, os

from historia.country import Country, Province, create_country
from historia.pops import Pop, make_initial_pops, PopJob
from historia.economy import make_RGOs, RGOType, Good
from historia.map import WorldMap
from historia.enums import HexType, DictEnum
from historia.utils import Store, Timer
from historia.world.biome import Biome

from termcolor import colored
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, depth=6)
echo = pp.pprint


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DictEnum):
            return obj.ref()
        return json.JSONEncoder.default(self, obj)


class Historia(object):
    """
        Keeps track of everything in history, and the current time in history
        Responsible for exporting the data
        and for making new days
    """
    def __init__(self, map_data, debug=False):
        self.debug = debug

        self.map = WorldMap(map_data)
        self.map_data = map_data

        # set the current_day
        self.start_date = arrow.get(1, 1, 1)
        self.current_day = self.start_date

        # list of all countries that have ever existed
        self.countries = []

        self.stores = {
            'Country': Store(self.current_day),
            'Province': Store(self.current_day),
            'Pop': Store(self.current_day)
        }

        with Timer("Populating world with initial data", debug=self.debug):
            self.populate()

    @classmethod
    def from_data(cls, data, debug):
        "Starts Historia from data"
        return cls(data, debug)

    def next_day(self):
        "Advance another day, updating the change stores"
        self.simulate_day()
        self.current_day = self.current_day.replace(days=+1)

    def jump_forward(self, months=1):
        for i in range(months):
            self.simulate_day()
        self.current_day = self.current_day.replace(months=months)

    def get_day(self):
        "Get today"
        return {
            'day': self.current_day.format("YYYY-MM-DD"),
            'data': {
                'Country': {c.id: c.export() for c in self.countries},
                'Province': {p.id: p.export() for c in self.countries for p in c.provinces},
                'Pop': {p.id: p.export() for c in self.countries for p in c.pops}
            }
        }

    def simulate_day(self):
        "Simulates a single day"
        markets = [p.market for c in self.countries for p in c.provinces]
        # date = '{}'.format(self.current_day.format('dddd MMMM D, YYYY'))
        # if self.current_day.datetime.day == 1:
        # print('→ {}:'.format(colored(date, 'blue', attrs=['bold', 'underline'])))

        # get every market in the world

        if self.current_day.datetime.day == 10:
            for c in self.countries:
                c.settle_frontier()

        for m in markets:
            # perform production and trading
            with Timer("simulate") as t:
                m.simulate()

        # update VAT
        for c in self.countries:
            c.determine_tax_policy()

    def populate(self):
        """
        Populate the map with some initial data.
        Make between 5 and 10 random countries owning one hex
        Make random pops for each country
        """

        NUM_COUNTRIES = 2 # random.randint(1, 4)

        # find a suitable hex
        with Timer("Creating initial data", debug=self.debug):

            for i in range(NUM_COUNTRIES):
                country, provinces, pops = create_country(self, self.map)
                country.determine_tax_policy()
                self.countries.append(country)

    @property
    def enums(self):
        return {
            'PopJob': PopJob.export_all(),
            'Biome': Biome.export_all(),
            'Good': Good.export_all()
        }

    @property
    def world_data(self):
        "World data needed for Explorer"
        return {
            'details': self.map_data.get('details'),
            'enums': self.enums,
            'geoforms': self.map_data.get('geoforms'),
            'hexes': [[i.reference for i in row] for row in self.map.hex_map]
        }
