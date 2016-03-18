from unittest import TestCase

from historia.condition import All, Any

from collections import namedtuple
test_scope = namedtuple('test_scope', 'a, b, c, d')


class TestCondition(TestCase):

    def test_condition(self):
        test_scope.a = 1
        test_scope.b = 1000
        test_scope.c = True

        c1 = All(
            test_scope.a <= 3,
            Any(
                test_scope.b > 500,
                test_scope.c is False
            )
        )
        self.assertEqual(c1, True)


if __name__ == '__main__':
    unittest.main()
