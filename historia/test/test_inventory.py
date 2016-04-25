from unittest import TestCase

from historia.pops.models.inventory import Inventory, NoInventorySpaceException
from historia.economy.enums.resource import Good

class TestInventory(TestCase):

    def test_inventory_list(self):
        inv = Inventory(10)
        inv.set(Good.grain, 5, 1.5)
        self.assertTrue(inv.add(Good.tools, 2, 3.25))
        self.assertTrue(inv.add(Good.tools, 3, 4.25))
        g1 = inv.get(Good.grain)
        g2 = inv.get(Good.tools)
        self.assertEqual(g1[0].amount, 5)
        self.assertEqual(g1[0].price, 1.5)
        self.assertEqual(g2[0].amount, 2)
        self.assertEqual(g2[0].price, 3.25)
        self.assertEqual(g2.amount, 5)
        self.assertEqual(g2.price, 7.5)

        inv.add(Good.iron_ore, 1)
        inv.add(Good.iron_ore, 1)
        self.assertEqual(len(inv.get(Good.iron_ore)), 1)

        inv.add(Good.iron_ore, 1, 1)
        inv.add(Good.iron_ore, 2, 2)
        self.assertEqual(len(inv.get(Good.iron_ore)), 3)

        self.assertEqual(inv.get_amount(Good.fish), 0)

    def test_subtract(self):
        inv = Inventory(10)
        inv.add(Good.grain, 10)
        self.assertTrue(inv.subtract(Good.grain, 1))
        self.assertEqual(inv.get(Good.grain).amount, 9)
        self.assertFalse(inv.subtract(Good.grain, 10))

    def test_space(self):
        inv = Inventory(10)
        self.assertFalse(inv.add(Good.grain, 11, 1))

        inv = Inventory(10)
        inv.add(Good.grain, 1, 1)
        self.assertFalse(inv.add(Good.grain, 10, 1))

        inv = Inventory(100)
        inv.add(Good.grain, 75)
        self.assertEqual(inv.used_space, 75)
        self.assertEqual(inv.empty_space, 25)

    def test_get(self):
        inv = Inventory(10)
        inv.add(Good.grain, 5)

        # get grain in inventory
        self.assertEqual(inv.get(Good.grain).amount, 5)

        # no iron ore in inventory
        self.assertEqual(inv.get(Good.iron_ore), None)

    def test_ideal(self):
        inv = Inventory(10)
        inv.add(Good.grain, 5)
        inv.add(Good.timber, 5)
        inv.add(Good.iron_ore, 5)

        # set ideal inventory
        inv.set_ideal(Good.grain, 10)
        inv.set_ideal(Good.timber, 1)
        inv.set_ideal(Good.tools, 10)

        # get ideal inventory
        self.assertEqual(inv.get_ideal(Good.grain), 10)

        # surplus
        self.assertEqual(inv.surplus(Good.timber), 4)
        self.assertEqual(inv.surplus(Good.iron), 0)

        # no ideal set, surplus is 100% of amount
        self.assertEqual(inv.surplus(Good.iron_ore), 5)

        # shortage
        self.assertEqual(inv.shortage(Good.grain), 5)

        # no shorage set
        self.assertEqual(inv.shortage(Good.iron_ore), 0)

        # no tools, so shortage is equal to ideal
        self.assertEqual(inv.shortage(Good.tools), 10)


if __name__ == '__main__':
    unittest.main()
