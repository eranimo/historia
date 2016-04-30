from random import random

class LogicBase:
    def __init__(self, pop):
        self.pop = pop

    @property
    def can_work(self):
        return True

    def has_good(self, good, amount):
        "Returns True if the Pop has a particular Good in their inventory"
        inv = self.pop.inventory.get(good)
        if inv is None:
            return False
        return inv.amount <= amount

    def get_good(self, good):
        "Gets a particular Good in a Pops inventory"
        i = self.pop.inventory.get(good)
        if i is None or i.amount == 0:
            return None
        return i

    def charge_idle_money(self):
        "Change a Pop's money"
        charge = 2
        # print("{} charged {} for being idle".format(self.pop.pop_job.title, charge))
        self.pop.money -= charge

    def consume(self, good, amount, chance=1):
        "Consumes a good in a chance"
        # print("{} consumed {} {}".format(self.pop.pop_job.title, amount, good.title))
        if random() <= chance:
            # print('consume', good, amount)
            return self.pop.inventory.subtract(good, amount)

    def produce(self, good, amount, chance=1):
        "Produces a good in a chance"
        # print("{} produced {} {}".format(self.pop.pop_job.title, amount, good.title))
        if random() <= chance:
            # print('produce', good, amount)
            return self.pop.inventory.add(good, amount)

    def perform(self):
        raise NotImplemented("LogicBase.perform implemented in inherited classes")
