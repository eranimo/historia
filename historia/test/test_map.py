from unittest import TestCase

from historia.map import WorldMap
from historia.hex import Hex
from historia.test.mocks import mock_map

h0_0_r = mock_map.find_hex(0, 0)

h0_0 = mock_map.find_hex(0, 0)
h0_1 = mock_map.find_hex(0, 1)
h0_2 = mock_map.find_hex(0, 2)

h1_0 = mock_map.find_hex(1, 0)
h1_1 = mock_map.find_hex(1, 1)
h1_2 = mock_map.find_hex(1, 2)

h2_0 = mock_map.find_hex(2, 0)
h2_1 = mock_map.find_hex(2, 1)
h2_2 = mock_map.find_hex(2, 2)


class TestWorldMap(TestCase):

    def test_hex_equality(self):
        self.assertEqual(h0_0 == h0_0_r, True, "Hex equality function not working")

    def test_hex_navigation(self):
        self.assertEqual(h1_1.hex_east, h1_2)
        self.assertEqual(h1_1.hex_west, h1_0)
        self.assertEqual(h1_1.hex_north_east, h0_2)
        self.assertEqual(h1_1.hex_north_west, h0_1)
        self.assertEqual(h1_1.hex_south_east, h2_2)
        self.assertEqual(h1_1.hex_south_west, h2_1)

if __name__ == '__main__':
    unittest.main()
