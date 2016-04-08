"""
Inventory class if I decide that Pops should keep track
of the price they paid for each good in their inventory
and that Inventory should be limited
"""

from collections import namedtuple
from statistics import mean
from historia.utils import unique_id

InventoryItem = namedtuple('InventoryItem', ['amount', 'price'])


class InventoryList(object):
    def __init__(self, *args):
        self._list = list(args)
        self.id = unique_id('he')

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __len__(self):
        return len(self._list)

    def avg_price(self):
        return mean([i.price for i in self._list])

    def list(self):
        return self._list

    def _clean(self):
        self._list = [l for l in self._list if l.amount > 0]

    def add(self, amount, price=None):
        "Adds a InventoryItem to this InventoryList, updates if an equal price already exists"
        if price in [i.price for i in self._list]:
            for index, item in enumerate(self._list):
                if item.price == price:
                    self._list[index] = InventoryItem(item.amount + amount, item.price)
                    break
        else:
            self._list.append(InventoryItem(amount, price))

        # remove empty InventoryItems
        self._clean()

    def subtract(self, amount):
        left = amount
        for index, item in enumerate(self._list):
            if item.amount < left: # not enough in this InventoryItem, take all of it
                new_amount = 0
                left -= item.amount
            elif item.amount >= left: # more than enough in this InventoryItem, take some of it
                new_amount = item.amount - left
                left = item.amount - left

            self._list[index] = InventoryItem(new_amount, item.price)

            if left == 0:
                break

        # remove empty InventoryItems
        self._clean()

    @property
    def amount(self):
        return sum(i.amount for i in self._list)

    @property
    def price(self):
        if all(i.price is None for i in self._list):
            return None
        return sum(i.price for i in self._list if i.price is not None)

    def __repr__(self):
        return "<InventoryList amount={} price={}>".format(self.amount, self.price)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())


class NoInventorySpaceException(Exception):
    pass


class Inventory(object):
    """
    An inventory is a dict of Good keys to namedtuple values.
    This dict has the following values:
    - amount (int)          The amount of the given good in the inventory
    - price (int, None)     The price of the good when it was purchased. None if produced

    Parameters:
    - space (int)            Max # units for each Good
    """
    def __init__(self, space):
        self.inventory = {}
        self.ideal = {}
        self.space = space
        self.id = unique_id('he')

    def has_item(self, good):
        "Returns True if the Inventory has a Good"
        try:
            self.inventory[good]
            return True
        except KeyError:
            return False

    def set_ideal(self, good, ideal):
        "Sets the ideal amount of goods in an inventory slot"
        self.ideal[good] = ideal

    def get_ideal(self, good):
        "Gets the ideal amount of goods in an inventory slot"
        if good in self.ideal:
            return self.ideal[good]
        return 0

    def surplus(self, good):
        "Returns # of units above the desired inventory"
        if self.get_amount(good) > self.get_ideal(good):
            return self.get_amount(good) - self.get_ideal(good)
        return 0

    def shortage(self, good):
        "Returns the # of units below the desired inventory"
        # if there is none of this good in the inventory, the shortage is the ideal
        if self.get(good) is None:
            return self.get_ideal(good)
        # if the amount is less than the ideal, the difference is the shortage
        if self.get_amount(good) < self.get_ideal(good):
            return self.get_ideal(good) - self.get_amount(good)
        return 0

    def get(self, good):
        "Get an InventoryItem in the inventory"
        if good not in self.inventory:
            return None
        return self.inventory[good]

    def get_amount(self, good):
        "Gets the total amount of a good in the inventory"
        item = self.get(good)
        if item:
            return item.amount
        return 0

    def set(self, good, amount, unit_price=None):
        "Sets inventory for a specific good"
        self.inventory[good] = InventoryList(InventoryItem(amount, unit_price))

    def add(self, good, amount, unit_price=None):
        "Add to the inventory by an amount"
        if self.has_item(good):
            if self.inventory[good].amount + amount <= self.space:
                self.inventory[good].add(amount, unit_price)
                return True
            else:
                return False
        else:
            if amount <= self.space:
                self.inventory[good] = InventoryList(InventoryItem(amount, unit_price))
                return True
            else:
                return False

    def subtract(self, good, amount):
        if self.has_item(good) and self.get(good).amount >= amount:
            self.get(good).subtract(amount)
            return True
        # didn't have item
        return False

    @property
    def empty_space(self):
        return self.space - self.used_space

    @property
    def used_space(self):
        return sum([i.amount for i in self.inventory.values()])

    def __repr__(self):
        return "<Inventory space={}>".format(self.space)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())

    def display(self):
        return ', '.join(['{}: ({})'.format(good.title, il.amount) for good, il in self.inventory.items()])

    def export(self):
        return [{'good': good.ref(), 'contents': [{'amount': i.amount, 'price': i.price} for i in il]} for good, il in self.inventory.items()]
