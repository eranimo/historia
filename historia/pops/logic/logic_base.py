from random import random

class LogicBase:
    def __init__(self, pop):
        self.pop = pop

    def has_good(self, good, amount):
        "Returns True if the Pop has a particular Good in their inventory"
        inv = self.pop.inventory.get(good)
        if inv is None:
            return False
        return inv.amount <= amount

    def get_good(self, good):
        "Gets a particular Good in a Pops inventory"
        return self.pop.inventory.get(good)

    def change_money(self, amount):
        "Change a Pop's money"
        self.pop.money += amount

    def consume(self, good, amount, chance=1):
        "Consumes a good in a chance"
        if random() <= chance:
            # print('consume', good, amount)
            return self.pop.inventory.subtract(good, amount)

    def produce(self, good, amount, chance=1):
        "Produces a good in a chance"
        if random() <= chance:
            # print('produce', good, amount)
            return self.pop.inventory.add(good, amount)

    def perform(self):
        raise NotImplemented("LogicBase.perform implemented in inherited classes")
