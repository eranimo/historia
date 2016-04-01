import random
import time
import arrow
import json

from historia.time import TimelineProperty
from historia.country import Country, Province
from historia.pops import Pop, make_random_pop, PopType
from historia.economy import make_RGOs, RGOType, Good
from historia.map import WorldMap
from historia.world import give_hex_natural_resources
from historia.log import HistoryLogger
from historia.enums import HexType
from historia.utils import ChangeStore, Change, Timer

from termcolor import colored

default_params = {
    'start_date': arrow.get(1, 1, 1),
    'run_months': 1
}

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
echo = pp.pprint

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Change):
            return obj.export()
        return json.JSONEncoder.default(self, obj)

class Historia(object):
    """
        Keeps track of everything in history, and the current time in history
        Responsible for exporting the data
        and for making new days
    """
    def __init__(self, map_data, params={}):
        self.params = default_params
        self.params.update(params)
        for key, value in self.params.items():
            setattr(self, key, value)

        self.map = WorldMap(map_data)
        self.map_data = map_data

        # set the current_day
        self.current_day = self.start_date
        self.end_day = self.start_date.replace(months=+self.run_months)

        # list of all countries that have ever existed
        self.countries = []

        # list of all ethic that have ever existed
        self.ethnic_groups = []

        # list of all languages that have ever existed
        self.languages = []

        self.logger = HistoryLogger(self)

        self.stores = {
            'Country': ChangeStore(self.current_day),
            'Province': ChangeStore(self.current_day),
            'Pop': ChangeStore(self.current_day)
        }

        # temp
        self.people = set()

        with Timer("Populating world with initial data"):
            self._populate()

    def next_day(self):
        self.current_day = self.current_day.replace(days=+1)
        for storeName, store in self.stores.items():
            store.commit()
            store.next_day()


    def start(self):
        """
        Main simulation loop

        For each day:
        - loop over countries
        - loop over pops
        """
        while self.current_day <= self.end_day:
            date = '{}'.format(self.current_day.format('dddd MMMM D, YYYY'))
            print('→ {}:'.format(colored(date, 'blue', attrs=['bold', 'underline'])))
            self.next_day()


    def _populate(self):
        """
            Populate the map with some initial data.
            Make between 5 and 10 random countries owning one hex
            Make random pops for each country
        """

        # find a suitable hex
        with Timer("Finding suitable hexes"):
            favorable_hexes = sorted(self.map.hexes, key=lambda h: h.favorability, reverse=True)
            start_hex = favorable_hexes[0]

        # give the hex some natural resources
        with Timer("\tMaking natural resources"):
            give_hex_natural_resources(start_hex)
            echo(start_hex.natural_resources)

        with Timer("\tCreating a province and country"):
            country1 = Country(self, start_hex)
            country1.name = 'Elysium'

            self.stores['Country'].add(country1)
            self.countries.append(country1)

            # Give that province pops and RGOs
            province = country1.provinces[0]
            self.stores['Province'].add(province)

        with Timer("\tMaking Pops and RGOs"):
            pops = []
            a1 = make_random_pop(province, PopType.aristocrat)
            f1 = make_random_pop(province, PopType.farmer)
            #make_RGOs(province, RGOType.grain_farm, a1, f1)
            f2 = make_random_pop(province, PopType.farmer)


            a2 = make_random_pop(province, PopType.aristocrat)
            l1 = make_random_pop(province, PopType.laborer)
            l2 = make_random_pop(province, PopType.laborer)

            c1 = make_random_pop(province, PopType.craftsman)
            c2 = make_random_pop(province, PopType.craftsman)

            new_pops = [a1, f1, f2, a2, l1, l2, c1, c2]
            province.add_pops(new_pops)
            self.stores['Pop'].extend(new_pops)

        with Timer("\tMaking another province in another day"):
            self.next_day()

            country1.name = 'Rome'

            # add another provinces
            second_hex = favorable_hexes[1]
            new_province = country1.settle_hex(second_hex)
            self.stores['Province'].add(new_province)

        with Timer("\tMaking another country in another day"):
            self.next_day()

            country2 = Country(self, favorable_hexes[2])
            country2.name = 'Athens'

            self.stores['Country'].add(country2)
            self.countries.append(country2)

            # Give that province pops and RGOs
            province2 = country2.provinces[0]
            self.stores['Province'].add(province2)

        self.next_day()


    def export(self, output_file):
        "Export the data to JSON"
        with open(output_file, 'w') as outfile:
            data = {
                'details': self.map_data.get('details'),
                'geoforms': self.map_data.get('geoforms'),
                'hexes': self.map.export(),
                'enums': {
                    'PopType': PopType.ref_map(),
                    'Good': Good.ref_map(),
                    'RGOType': RGOType.ref_map()
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

            with Timer("Exporting to JSON"):
                json.dump(data, outfile, indent=2, cls=JsonEncoder)
