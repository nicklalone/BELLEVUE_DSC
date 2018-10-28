import unittest
import datetime
from msds510.utils import date


class DateTest(unittest.TestCase):

    def setUp(self):
        self.month_examples = ['Sep-80', '1990-Oct', 'Jan']
        self.year_examples = ['1980', '1990', '1900']

    def test_valid_get_month(self):
        self.assertEqual(date.get_month(self.month_examples[0]), 9)

    def test_valid_get_month2(self):
        self.assertEqual(date.get_month(self.month_examples[1]), 10)

    def test_valid_get_month3(self):
        self.assertEqual(date.get_month(self.month_examples[2]), 1)

    def test_valid_get_month4(self):
        self.assertEqual(date.get_month(''), None)

    def test_valid_get_date_joined(self):
        self.assertEqual(date.get_date_joined(
            self.year_examples[0],
            self.month_examples[0]),
            datetime.date(1980, 9, 1)
        )

    def test_valid_get_date_joined2(self):
        self.assertEqual(date.get_date_joined(
            self.year_examples[1],
            self.month_examples[1]),
            datetime.date(1990, 10, 1)
        )

    def test_valid_get_date_joined3(self):
        self.assertEqual(date.get_date_joined(
            self.year_examples[2],
            self.month_examples[2]),
            datetime.date(1900, 1, 1)
        )

    def test_valid_days_since_joined(self):
        self.assertAlmostEqual(date.days_since_joined(
            self.year_examples[0],
            self.month_examples[0]), 13782)

    def test_valid_days_since_joined2(self):
        self.assertAlmostEqual(date.days_since_joined(
            self.year_examples[1],
            self.month_examples[1]), 10100)

    def test_valid_days_since_joined3(self):
        self.assertAlmostEqual(date.days_since_joined(
            self.year_examples[2],
            self.month_examples[2]), 43245)


if __name__ == '__main__':
    unittest.main()
