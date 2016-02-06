import random

from historia.time import Day, TimelineProperty
from historia.country import Country
from historia.map import WorldMap

default_params = {
    'start_date': Day(1, 1, 1),
    'run_years': 1
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
        self.end_day = self.start_date.add(years=self.run_years)

        # list of all countries that have ever existed
        self.countries = []

        # list of all ethic that have ever existed
        self.ethnic_groups = []

        # list of all languages that have ever existed
        self.languages = []

        self._populate()

    def start(self):
        """
        Main simulation loop

        - loop over countries
        - check to see if any can run events, run those events
        """
        while self.current_day <= self.end_day:

            self.current_day.add(days=1)

    def _populate(self, ):
        """
            Populate the map with some initial data.
            Make a few countries scattered around the map
        """
        num_initial_countries = random.randint(5, 10)
        for i in xrange(num_initial_countries):
            h = self.map.random_hex()
            Country(self, initial_territory=[h])

    def report(self, ):
        """
            Report everything that happened on the current day
        """
        pass

    def export(self, file_path):
        """ Export the data to JSON """
        with open(newfile, 'w') as outfile:
            json.dumps()
        pass
