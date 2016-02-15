import random
import time
import arrow

from historia.time import TimelineProperty
from historia.country import Country
from historia.person import Person, find_spouse
from historia.map import WorldMap
from historia.log import HistoryLogger, LogEvent
from historia.enums import HexType

default_params = {
    'start_date': arrow.get(1, 1, 1),
    'run_years': 100
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

        - loop over countries
        - check to see if any can run events, run those events
        """
        new_babies = set()
        new_deaths = set()
        new_marriages = 0
        new_engages = 0
        num_sex = 0
        while self.current_day <= self.end_day:
            #print('')
            avg_age = 0
            for p in self.people:
                #print(p.stats)
                # TODO: these should be events

                # ENGAGEMENT
                # make sure everyone who can and wants to get married does
                if p.can_get_married:
                    # find breeding pairs
                    found_spouse = find_spouse(p, self.people)
                    if found_spouse:
                        new_engages += 1
                        p.get_engaged(found_spouse)
                # TODO: sex outside of marriage

                # MARRIAGE
                if p.is_engaged and p.check_marriage():
                    p.get_married()
                    num_sex += 1
                    new_marriages += 1

                # PREGNANCY
                if p.check_pregnancy():
                    # death from childbirth
                    if random.randint(0, 100) <= 2:
                        new_deaths.add(p)
                    else:
                        baby = p.have_baby()
                        new_babies.add(baby)

                # SEX
                if p.is_adult and self.current_day == p.next_sex:
                    p.have_sex(p.spouse)
                    num_sex += 1


                # RANDOM DEATH
                if random.randint(0, 1000000) < 24:
                    new_deaths.add(p)

                avg_age += p.age

            self.people.update(new_babies)
            self.people.difference_update(new_deaths)

            if self.current_day.day == 1:
                print("{}, {}, {}, {}, {}, {}, {}".format(
                    self.current_day.format('MMMM YYYY'),
                    len(self.people),
                    len(new_babies),
                    len(new_deaths),
                    int(round(avg_age / float(len(self.people)))),
                    new_marriages,
                    new_engages,
                    num_sex
                ))
                new_babies = set()
                new_deaths = set()
                new_marriages = 0
                new_engages = 0
                num_sex = 0
                avg_age = 0

            self.current_day = self.current_day.replace(days=+1)


    def _populate(self, ):
        """
            Populate the map with some initial data.
            Make some Persons
        """
        for i in xrange(0, 10):
            self.people.add(Person.new_adult(self))

        # num_initial_countries = random.randint(5, 10)
        # for i in xrange(num_initial_countries):
        #     h = self.map.random_hex(type=HexType.land)
        #     country = Country(self, h)
        #     self.countries.append(country)

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
