import random
import time
import arrow
import json

from historia.time import TimelineProperty
from historia.country import Country, Province, create_country
from historia.pops import Pop, make_initial_pops, PopType
from historia.economy import make_RGOs, RGOType, Good
from historia.map import WorldMap
from historia.log import HistoryLogger
from historia.enums import HexType, DictEnum
from historia.utils import Store, Change, Timer

from termcolor import colored

default_params = {
    'start_date': arrow.get(1, 1, 1),
    'run_days': 100
}

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, depth=6)
echo = pp.pprint


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Change):
            return obj.export()
        if isinstance(obj, DictEnum):
            return obj.ref()
        return json.JSONEncoder.default(self, obj)


class Historia(object):
    """
        Keeps track of everything in history, and the current time in history
        Responsible for exporting the data
        and for making new days
    """
    def __init__(self, map_data, debug=False, params={}):
        self.params = default_params
        self.debug = debug
        self.params.update(params)
        for key, value in self.params.items():
            setattr(self, key, value)

        self.map = WorldMap(map_data)
        self.map_data = map_data

        # set the current_day
        self.current_day = self.start_date
        self.end_day = self.start_date.replace(days=+self.run_days)
        print("Running for {} days".format(self.run_days))

        # list of all countries that have ever existed
        self.countries = []

        # list of all ethic that have ever existed
        self.ethnic_groups = []

        # list of all languages that have ever existed
        self.languages = []

        self.logger = HistoryLogger(self)

        self.stores = {
            'Country': Store(self.current_day),
            'Province': Store(self.current_day),
            'Pop': Store(self.current_day)
        }

        # temp
        self.people = set()

        with Timer("Populating world with initial data", debug=self.debug):
            self.populate()

    def next_day(self):
        "Advance another day, updating the change stores"
        self.current_day = self.current_day.replace(days=+1)
        for storeName, store in self.stores.items():
            store.update()
            store.next_day()

    def start(self):
        """
        Main simulation loop

        For each day:
        - loop over countries
        - loop over pops
        """

        while self.current_day <= self.end_day:
            markets = [p.market for c in self.countries for p in c.provinces]
            date = '{}'.format(self.current_day.format('dddd MMMM D, YYYY'))
            # if self.current_day.datetime.day == 1:
            print('→ {}:'.format(colored(date, 'blue', attrs=['bold', 'underline'])))

            # get every market in the world

            if self.current_day.datetime.day == 10:
                for c in self.countries:
                    c.settle_frontier()

            for m in markets:
                # perform production and trading
                m.simulate()

            self.next_day()

        for storeName, store in self.stores.items():
            store.update()

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
                self.stores['Country'].add(country)
                self.stores['Province'].add(provinces)
                self.stores['Pop'].add(pops)
                self.countries.append(country)

        # with Timer("\tMaking another province in another day", debug=self.debug):
        #     self.next_day()
        #
        #     country1.name = 'Rome'
        #
        #     # add another provinces
        #     second_hex = favorable_hexes[1]
        #     new_province = country1.settle_hex(second_hex)
        #     self.stores['Province'].add(new_province)
        #
        # with Timer("\tMaking another country in another day", debug=self.debug):
        #     self.next_day()
        #
        #     country2 = Country(self, favorable_hexes[2])
        #     country2.name = 'Athens'
        #
        #     self.stores['Country'].add(country2)
        #     self.countries.append(country2)
        #
        #     # Give that province pops and RGOs
        #     province2 = country2.provinces[0]
        #     self.stores['Province'].add(province2)

        self.next_day()


    def export(self, output_file):
        "Export the data to JSON"
        with open(output_file, 'w') as outfile:
            data = {
                'details': self.map_data.get('details'),
                'geoforms': self.map_data.get('geoforms'),
                'hexes': self.map.export(),
                'enums': {
                    'PopType': PopType.export_all(),
                    'Good': Good.export_all()
                },
                'times': {
                    'start_day': self.start_date.format("YYYY-MM-DD"),
                    'end_day': self.stores['Country'].tick.format("YYYY-MM-DD")
                },
                'data': {
                    'Country': {}, # {c.id: c.export() for c in self.countries},
                    'Province': {}, # {p.id: p.export() for c in self.countries for p in c.provinces},
                    'Pop': {} # {p.id: p.export() for c in self.countries for p in c.pops}
                },
                'timeline': {}
            }
            for storeName, store in self.stores.items():
                data['timeline'][storeName] = store.export()

            with Timer("Exporting to JSON", debug=self.debug):
                json.dump(data, outfile, indent=2, cls=JsonEncoder)

        # with open('./bin/timeline.json', 'w') as timeline_file:
        #     json.dump(data['timeline'], timeline_file, indent=2, cls=JsonEncoder)
