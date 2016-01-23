from historia.time import Day, TimelineProperty
from historia.map import WorldMap

default_params = {
    'start_date': Day(1, 1, 1)
}

class Historia:
    """
        Manager class for the entire program.
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

        # list of all countries that have ever existed
        self.countries = []

        # list of all ethic that have ever existed
        self.ethnic_groups = []

        # list of all languages that have ever existed
        self.languages = []

    def populate():
        """
            Populate the map with some initial data.
            Make Countries,
        """

    def step():
        """
            Start history
        """
        self.current_day.next()

    def report():
        """
            Report everything that happened on the current day
        """
        pass

    def export(all=False):
        pass
