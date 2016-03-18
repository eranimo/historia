import random
import time
import arrow

from historia.time import TimelineProperty
from historia.country import Country
from historia.pops import Pop, make_random_pop
from historia.map import WorldMap
from historia.log import HistoryLogger, LogEvent
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
        start_hex = favorable_hexes[0]

        # create a province and country
        start_country = Country(self, start_hex)
        self.countries.append(start_country)

        # Give that province pops and RGOs
        province = start_country.provinces[0]
        pops = []
        a1 = make_random_pop(province, PopType.aristocrat)
        f1 = make_random_pop(province, PopType.farmer)
        f2 = make_random_pop(province, PopType.farmer)

        a2 = make_random_pop(province, PopType.aristocrat)
        l1 = make_random_pop(province, PopType.laborer)
        l2 = make_random_pop(province, PopType.laborer)

        c1 = make_random_pop(province, PopType.craftsman)
        c2 = make_random_pop(province, PopType.craftsman)



        print('Hex: {}'.format(start_hex))
        print('Country: {}'.format(start_country))
        print(colored('Pops:', 'blue'))
        echo(start_country.pops)



    def export(self, file_path):
        """
            Export the data to JSON

            # Structure
            {
                map_data: object, # map data like size and Hexgen options
                hexes: [Hex, ...], # all hexes on map
                data: { # DB of entities that have existed
                    countries: [Country, ...]
                    cultures: [Culture, ...]
                    religions: [Religion, ...]
                },
                timeline: [ # changes to those entities
                    {
                        'day': DateTime
                        'event': TimelineEvent object,
                        'entity_name': String,
                        'entity_id': Integer
                    }
                ]
            }




        """
        # with open(newfile, 'w') as outfile:
        #     json.dumps()
        pass
