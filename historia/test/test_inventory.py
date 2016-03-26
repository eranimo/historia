from unittest import TestCase

from historia.pops.models.inventory import Inventory, NoInventorySpaceException
from historia.economy.enums.resource import Good

class TestInventory(TestCase):

    def test_set(self):
        inventory = Inventory(10)
        inventory.set(Good.grain, 5, 1.5)
        g = inventory.get(Good.grain)
        self.assertEqual(g[0].amount, 5)
        self.assertEqual(g[0].price, 1.5)
        self.assertEqual(g.space, 5)

    def test_add(self):
        inventory = Inventory(10)
        with self.assertRaises(NoInventorySpaceException):
            inventory.add(Good.grain, 11, 1)

        inventory = Inventory(10)
        inventory.add(Good.grain, 1, 1)
        with self.assertRaises(NoInventorySpaceException):
            inventory.add(Good.grain, 10, 1)


if __name__ == '__main__':
    unittest.main()
