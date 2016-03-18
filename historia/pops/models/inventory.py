"""
Inventory class if I decide that Pops should keep track
of the price they paid for each good in their inventory
and that Inventory should be limited
"""

from collections import namedtuple
from statistics import mean

InventoryItem = namedtuple('InventoryItem', ['amount', 'price'])


class InventoryList(object):
    def __init__(self, *args):
        self._list = args

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self):
        raise NotImplemented("Can't set an inventory list")

    def __len__(self):
        return len(self._list)

    def avg_price(self):
        return mean([i.price for i in self._list])

    def list(self):
        return self._list

    def add(self, amount, price=None):
        self._list.append(InventoryItem(amount, price))

    @property
    def space(self):
        return sum(i.amount for i in self._list)


class NoInventorySpaceException(Exception):
    pass


class Inventory(object):
    """
    An inventory is a dict of Resource keys to namedtuple values.
    This dict has the following values:
    - amount (int)          The amount of the given resource in the inventory
    - price (int, None)     The price of the good when it was purchased. None if produced

    Parameters:
    - size (int)            Max # units for each Resource
    """
    def __init__(self, size):
        self.inventory = {}
        self.size = size

    def has_item(self, resource):
        "Returns True if the Inventory has a Resource"
        try:
            self.inventory[resource]
            return True
        except KeyError:
            return False

    def get(self, resource):
        "Get an InventoryItem in the inventory"
        return self.inventory[resource]

    def set(self, resource, amount, price=None):
        "Sets inventory for a specific resource"
        self.inventory[resource] = InventoryList(InventoryItem(amount, price))

    def add(self, resource, amount, price=None):
        "Add to the inventory by an amount"
        if self.has_item(resource):
            if self.inventory[resource].space + amount <= self.size:
                self.inventory[resource].add(amount, price)
            else:
                raise NoInventorySpaceException("No more room in inventory")
        else:
            if amount <= self.size:
                self.inventory[resource] = InventoryList(InventoryItem(amount, price))
            else:
                raise NoInventorySpaceException("No more room in inventory")
