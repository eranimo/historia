from unittest import TestCase

from historia.time import Day, TimelineProperty
from historia.test.mocks import mock_manager
from historia.errors import CalendarError

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
        """ Test day comparison """
        self.assertEqual(d1, d1_1, "Days of equal values should be considered equal")
        self.assertEqual(d1 < d2, True, "< method not working")
        self.assertEqual(d1 <= d1, True, "<= method not working")
        self.assertEqual(d2 > d1, True, "> method not working")
        self.assertEqual(d2 >= d2, True, ">= method not working")
        self.assertEqual(d1 == d1, True, "= method not working")
        self.assertEqual(d1 == d2, False, "= method not working")
        self.assertEqual(d1 != d2, True, "!= method not working")

    def test_day_add(self):
        """ Test day addition """
        self.assertEqual(Day(1, 1, 1).add(days=1), Day(2, 1, 1))
        self.assertEqual(Day(1, 1, 1).add(days=30), Day(1, 2, 1))
        self.assertEqual(Day(1, 1, 1).add(days=65), Day(6, 3, 1))
        self.assertEqual(Day(1, 1, 1).add(days=360), Day(1, 1, 2))

        self.assertEqual(Day(1, 1, 1).add(months=1), Day(1, 2, 1))
        self.assertEqual(Day(1, 1, 1).add(months=12), Day(1, 1, 2))
        self.assertEqual(Day(1, 1, 1).add(months=25), Day(1, 2, 3))

        self.assertEqual(Day(1, 1, 1).add(years=1), Day(1, 1, 2))
        self.assertEqual(Day(1, 1, 1).add(years=100), Day(1, 1, 101))

        self.assertEqual(Day(1, 1, 1).add(days=3, months=1, years=4), Day(4, 2, 5))

    def test_display(self):
        self.assertEqual(Day(1, 1, 1).display(), 'January 1st, year 1')
        self.assertEqual(Day(29, 12, 1).display(), 'December 29th, year 1')
        self.assertEqual(Day(3, 12, 1).display(), 'December 3rd, year 1')
        self.assertEqual(Day(2, 2, 100).display(), 'February 2nd, year 100')

    def test_diff(self):
        self.assertEqual(Day(2, 1, 1).diff(Day(1, 1, 1)), dict(days=1, months=0, years=0))
        self.assertEqual(Day(1, 5, 1).diff(Day(1, 2, 1)), dict(days=0, months=3, years=0))

    # def test_day_subtract(self):
    #     """ Test day subtraction """
    #     self.assertEqual(Day(10, 1, 1).subtract(days=1), Day(9, 1, 1))
    #     self.assertEqual(Day(10, 2, 1).subtract(days=11), Day(29, 1, 1))
    #     self.assertEqual(Day(1, 1, 2).subtract(days=10), Day(20, 12, 1))
    #
    #     with self.assertRaises(CalendarError):
    #         Day(10, 1, 1).subtract(days=11)
    #     with self.assertRaises(CalendarError):
    #         Day(10, 1, 1).subtract(months=1)
    #     with self.assertRaises(CalendarError):
    #         Day(10, 1, 1).subtract(years=1)


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
