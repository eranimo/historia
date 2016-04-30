from unittest import TestCase

from historia.pops.enums.pop_job import PopJob
from historia.economy import Good
from historia.test.mocks import mock_manager, mock_map, make_mock_country, make_mock_pop


random_hex = mock_map.random_hex()
country = make_mock_country(mock_manager, random_hex)
province = country.provinces[0]
market = province.market


class TestEconomy(TestCase):
    def test_money(self):
        farmer = make_mock_pop(province, PopJob.farmer)
        province.add_pops([farmer])

        farmer.money += 10
        self.assertEqual(farmer.money, 20)
        farmer.money -= 10
        self.assertEqual(farmer.money, 10)

    def test_idle_fee(self):
        farmer = make_mock_pop(province, PopJob.farmer)
        province.add_pops([farmer])

        farmer.inventory.set(Good.timber, 0)
        self.assertEqual(farmer.money, 10)
        farmer.perform_production()
        self.assertEqual(farmer.money, 8)

    def test_production(self):
        farmer = make_mock_pop(province, PopJob.farmer)
        province.add_pops([farmer])

        grain = farmer.inventory.get_amount(Good.grain)
        tools = farmer.inventory.get_amount(Good.tools)
        bread = farmer.inventory.get_amount(Good.bread)
        timber = farmer.inventory.get_amount(Good.timber)

        farmer.perform_production()

        self.assertEqual(farmer.inventory.get_amount(Good.grain), grain + 4)
        self.assertEqual(farmer.inventory.get_amount(Good.bread), bread - 1)
        self.assertEqual(farmer.inventory.get_amount(Good.timber), timber - 1)

        farmer.inventory.add(Good.timber, 1)
        farmer.inventory.add(Good.bread, 1)

        grain = farmer.inventory.get_amount(Good.grain)
        tools = farmer.inventory.get_amount(Good.tools)
        bread = farmer.inventory.get_amount(Good.bread)
        timber = farmer.inventory.get_amount(Good.timber)


        farmer.perform_production()

        self.assertEqual(farmer.inventory.get_amount(Good.grain), grain + 4)
        self.assertEqual(farmer.inventory.get_amount(Good.bread), bread - 1)
        self.assertEqual(farmer.inventory.get_amount(Good.timber), timber - 1)
