from unittest import TestCase

from historia.time import Day

class TestDay(TestCase):

    def test_day(self):
        d1 = Day(1, 1, 1)
        d1_1 = Day(1, 1, 1)
        d2 = Day(2, 1, 1)
        d3 = Day(10, 10, 10)
        self.assertEqual(d1, d1_1, "Days of equal values should be considered equal")

if __name__ == '__main__':
    unittest.main()
