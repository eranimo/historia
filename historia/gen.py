import random
import time
import arrow
import json

from historia.time import TimelineProperty
from historia.country import Country
from historia.pops import Pop, make_random_pop, PopType
from historia.economy import make_RGOs, RGOType, Good
from historia.map import WorldMap
from historia.world import give_hex_natural_resources
from historia.log import HistoryLogger
from historia.enums import HexType

from termcolor import colored

default_params = {
    'start_date': arrow.get(1, 1, 1),
    'run_months': 1
}

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
echo = pp.pprint

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


        # temp
        self.people = set()

        self._populate()


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
            self.current_day = self.current_day.replace(days=+1)


    def _populate(self):
        """
            Populate the map with some initial data.
            Make between 5 and 10 random countries owning one hex
            Make random pops for each country
        """

        # find a suitable hex
        favorable_hexes = sorted(self.map.hexes, key=lambda h: h.favorability, reverse=True)
        start_hex = favorable_hexes[1]

        # give the hex some natural resources
        give_hex_natural_resources(start_hex)
        print('Hex natural resources:')
        echo(start_hex.natural_resources)

        # create a province and country
        start_country = Country(self, start_hex)
        start_country.name = 'Elysium'
        self.countries.append(start_country)

        # Give that province pops and RGOs
        province = start_country.provinces[0]
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

        province.add_pops([a1, f1, f2, a2, l1, l2, c1, c2])

        print('Hex: {}'.format(start_hex))
        print('Country: {}'.format(start_country))
        print(colored('Pops:', 'blue'))
        echo(province.pops)



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
                'data': {
                    'Country': {c.id: c.export() for c in self.countries},
                    'Province': {p.id: p.export() for c in self.countries for p in c.provinces},
                    'Pop': {p.id: p.export() for c in self.countries for p in c.pops}
                },
                'timeline': self.logger.export()
            }
            json.dump(data, outfile, indent=2)
