from unittest import TestCase

from historia.time import TimelineProperty
from historia.test.mocks import mock_manager
from historia.errors import CalendarError
#
#
# class TestTimelineProperty(TestCase):
#
#     def test_timeline_set(self):
#         t1 = []
#         tp1 = TimelineProperty(mock_manager, t1)
#         tp1.set(d1, 1)
#         tp1.set(d3, 5)
#         self.assertEqual(tp1.timeline[0][0], d1)
#         self.assertEqual(tp1.timeline[0][1], 1)
#         self.assertEqual(tp1.timeline[1][0], d3)
#         self.assertEqual(tp1.timeline[1][1], 5)
#
#     def test_timeline_get(self):
#         t1 = []
#         tp1 = TimelineProperty(mock_manager, t1)
#         tp1.set(d1, 1)
#         tp1.set(d3, 5)
#         t_1 = tp1.get(d1)
#         t_1_1 = tp1.get(d1_1)
#         t_3 = tp1.get(d3)
#         t_3_1 = tp1.get(d3_1)
#         error_message = lambda x, y: "Timeline get not getting correct value. Got {} but expected {}".format(x, y)
#         self.assertEqual(t_1 == 1, True, error_message(t_1, 1))
#         self.assertEqual(t_1_1 == 1, True, error_message(t_1_1, 1))
#         self.assertEqual(t_3 == 5, True, error_message(t_3, 5))
#         self.assertEqual(t_3_1 == 5, True, error_message(t_3, 5))
#

if __name__ == '__main__':
    unittest.main()
