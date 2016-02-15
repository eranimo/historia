from unittest import TestCase

from historia.person import Person, find_spouse, Gender
from historia.test.mocks import mock_manager

people = []
for i in xrange(0, 100):
    people.append(Person.new_adult(mock_manager))
people[0].gender = Gender.female


p = people[0]

class TestPerson(TestCase):

    def test_find_spouse(self):
        # self.assertEqual(tp1.timeline[1][1], 5)
        found = find_spouse(p, people)
        if found:
            p.get_engaged(found)
            self.assertEqual(p.engaged_to, found)
            self.assertEqual(p.can_get_married, False)
            self.assertEqual(p.engaged_to.engaged_to, p)
            self.assertEqual(p.is_engaged, True)

    def test_marriage(self):

        partner = p.engaged_to
        self.assertNotEqual(p.marriage_date, None)
        mock_manager.current_day = p.marriage_date
        p.get_married()
        self.assertEqual(p.engaged_to, None)
        self.assertEqual(p.marriage_date, None)
        self.assertEqual(p.spouse, partner)
        self.assertEqual(p.can_get_married, False)

        # have sex until pregnant
        while p.is_pregnant is False:
            p.have_sex(p.spouse)
        self.assertEqual(p.is_pregnant, True)
        self.assertEqual(p.baby_father, p.spouse)

    def test_pregnancy(self):
        due_date = mock_manager.current_day.replace(months=+9)
        self.assertEqual(p.baby_due_date, due_date)

        # can't have the baby before its due
        with self.assertRaises(Exception):
            p.have_baby()

        mock_manager.current_day = due_date
        baby = p.have_baby()
        self.assertEqual(baby in p.children, True)
        self.assertEqual(baby in p.spouse.children, True)
        self.assertEqual(p.is_pregnant, False)
        self.assertEqual(p.baby_due_date, None)
        self.assertEqual(p.baby_father, None)
        self.assertEqual(baby.birth_date, due_date)
        self.assertEqual(baby.mother, p)
        self.assertEqual(baby.father, p.spouse)
        self.assertEqual(baby.can_get_married, False)

        # age the baby up
        mock_manager.current_day = mock_manager.current_day.replace(years=+20)
        self.assertEqual(baby.can_get_married, True)
        self.assertEqual(baby.age, 20)


if __name__ == '__main__':
    unittest.main()
