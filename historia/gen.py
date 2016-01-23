from historia.time import Day, TimelineProperty

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
    def __init__(self):
        self.params = default_params
        self.params.update(params)

        self.days = []

        # list of all countries that have ever existed
        self.countries = []

        # list of all ethic that have ever existed
        self.ethnic_groups = []

        # list of all languages that have ever existed
        self.languages = []

        # set the current_day
        self.current_day = self.params.start_date

    def step():
        self.current_day.next()

    def report():
        """
            Report everything that happened on the current day
        """
        pass

    def export(all=False):
        pass
