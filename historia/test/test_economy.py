from unittest import TestCase

from historia.pops.enums.pop_type import PopType
from historia.economy import Good
from historia.test.mocks import mock_manager, mock_map, make_mock_country, make_mock_pop


random_hex = mock_map.random_hex()

country = make_mock_country(mock_manager, random_hex)
province = country.provinces[0]
market = province.market

farmer = make_mock_pop(province, PopType.farmer)
miner = make_mock_pop(province, PopType.miner)
miller = make_mock_pop(province, PopType.miller)
woodcutter = make_mock_pop(province, PopType.woodcutter)
blacksmith = make_mock_pop(province, PopType.blacksmith)
refiner = make_mock_pop(province, PopType.refiner)
baker = make_mock_pop(province, PopType.baker)
province.add_pops([farmer, miner, miller, woodcutter, blacksmith, refiner, baker])


class TestEconomy(TestCase):
    pass
    # def test_production(self):
    #     print(farmer.inventory.export())
    #     grain = farmer.inventory.get_amount(Good.grain)
    #     bread = farmer.inventory.get_amount(Good.bread)
    #     timber = farmer.inventory.get_amount(Good.timber)
    #     farmer.perform_production()
    #     self.assertEqual(farmer.inventory.get_amount(Good.grain), grain + 4)
    #     self.assertEqual(farmer.inventory.get_amount(Good.bread), bread - 1)
    #     self.assertEqual(farmer.inventory.get_amount(Good.timber), timber - 1)
