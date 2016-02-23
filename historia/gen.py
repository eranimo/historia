import random
import time
import arrow

from historia.time import TimelineProperty
from historia.country import Country
from historia.pops import Pop
from historia.map import WorldMap
from historia.log import HistoryLogger, LogEvent
from historia.enums import HexType

default_params = {
    'start_date': arrow.get(1, 1, 1),
    'run_years': 10
}

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
        self.end_day = self.start_date.replace(years=+self.run_years)

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

            if self.current_day.day == 1:
                print("{}".format(
                    self.current_day.format('MMMM YYYY')
                ))

            self.current_day = self.current_day.replace(days=+1)


    def _populate(self, ):
        """
            Populate the map with some initial data.
        """

        num_initial_countries = random.randint(5, 10)
        for i in xrange(num_initial_countries):
            h = self.map.random_hex(type=HexType.land)
            country = Country(self, h)
            self.countries.append(country)

    def report(self, ):
        """
            Report everything that happened on the current day
        """
        pass

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
