from unittest import TestCase

from historia.time import Day, TimelineProperty
from historia.test.mocks import mock_manager

d1 = Day(1, 1, 1)
d1_1 = Day(1, 1, 1)
d2 = Day(2, 1, 1)
d2_1 = Day(9, 10, 10)
d3 = Day(10, 10, 10)
d3_1 = Day(11, 10, 10)

class TestDay(TestCase):

    def test_day_stamp(self):
        self.assertEqual(d1.stamp, 9384, "Stamp value incorrect")

    def test_day_comparison(self):
        self.assertEqual(d1, d1_1, "Days of equal values should be considered equal")
        self.assertEqual(d1 < d2, True, "< method not working")
        self.assertEqual(d1 <= d1, True, "<= method not working")
        self.assertEqual(d2 > d1, True, "> method not working")
        self.assertEqual(d2 >= d2, True, ">= method not working")
        self.assertEqual(d1 == d1, True, "= method not working")
        self.assertEqual(d1 == d2, False, "= method not working")
        self.assertEqual(d1 != d2, True, "!= method not working")

class TestTimelineProperty(TestCase):

    def test_timeline_set(self):
        t1 = []
        tp1 = TimelineProperty(mock_manager, t1)
        tp1.set(d1, 1)
        tp1.set(d3, 5)
        self.assertEqual(tp1.timeline[0][0], d1)
        self.assertEqual(tp1.timeline[0][1], 1)
        self.assertEqual(tp1.timeline[1][0], d3)
        self.assertEqual(tp1.timeline[1][1], 5)

    def test_timeline_get(self):
        t1 = []
        tp1 = TimelineProperty(mock_manager, t1)
        tp1.set(d1, 1)
        tp1.set(d3, 5)
        t_1 = tp1.get(d1)
        t_1_1 = tp1.get(d1_1)
        t_3 = tp1.get(d3)
        t_3_1 = tp1.get(d3_1)
        error_message = lambda x, y: "Timeline get not getting correct value. Got {} but expected {}".format(x, y)
        self.assertEqual(t_1 == 1, True, error_message(t_1, 1))
        self.assertEqual(t_1_1 == 1, True, error_message(t_1_1, 1))
        self.assertEqual(t_3 == 5, True, error_message(t_3, 5))
        self.assertEqual(t_3_1 == 5, True, error_message(t_3, 5))


if __name__ == '__main__':
    unittest.main()
