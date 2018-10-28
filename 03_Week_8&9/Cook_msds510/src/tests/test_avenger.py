import unittest
import datetime
from msds510.avenger import Avenger


class AvengerTest(unittest.TestCase):

    def setUp(self):
        self.pym_record = {
            'appearances': '1269',
            'current': 'YES',
            'death1': 'YES',
            'death2': '',
            'death3': '',
            'death4': '',
            'death5': '',
            'full_reserve_avengers_intro': 'Sep-63',
            'gender': 'MALE',
            'honorary': 'Full',
            'name_alias': 'Henry Jonathan "Hank" Pym',
            'notes': 'Merged with Ultron in Rage of '
                     'Ultron Vol. 1. A funeral was held. \n',
            'probationary_introl': '',
            'return1': 'NO',
            'return2': '',
            'return3': '',
            'return4': '',
            'return5': '',
            'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
            'year': '1963',
            'years_since_joining': '52'
        }

        self.avenger = Avenger(self.pym_record)

    def test_valid_get_name_alias(self):
        self.assertEqual(self.avenger.name_alias(),
                         'Henry Jonathan "Hank" Pym')

    def test_invalid_get_name_alias(self):
        self.assertNotEqual(self.avenger.name_alias(),
                            'Other Name')

    def test_valid_get_url(self):
        self.assertEqual(self.avenger.url(),
                         'http://marvel.wikia.com/Henry_Pym_(Earth-616)')

    def test_invalid_get_url(self):
        self.assertNotEqual(self.avenger.url(),
                            'not url string')

    def test_valid_get_is_current(self):
        self.assertEqual(self.avenger.is_current(), True)

    def test_invalid_get_is_current(self):
        self.assertNotEqual(self.avenger.is_current(), False)

    def test_valid_get_gender(self):
        self.assertEqual(self.avenger.gender(), 'MALE')

    def test_invalid_get_gender(self):
        self.assertNotEqual(self.avenger.gender(), 'Male')

    def test_valid_get_year_joined(self):
        self.assertEqual(self.avenger.year(), 1963)

    def test_invalid_get_year_joined(self):
        self.assertNotEqual(self.avenger.year(),
                            "not a match")

    def test_valid_get_date_joined(self):
        self.assertEqual(self.avenger.date_joined(),
                         datetime.date(1963, 9, 1))

    def test_invalid_get_date_joined(self):
        self.assertNotEqual(self.avenger.date_joined(),
                            datetime.date(1965, 9, 1))

    def test_valid_get_days_since_joined(self):
        self.assertAlmostEqual(self.avenger.days_since_joining(), 19992)

    def test_invalid_get_days_since_joined(self):
        self.assertNotEqual(self.avenger.days_since_joining(), -1)

    def test_valid_get_years_since_joined(self):
        self.assertEqual(self.avenger.years_since_joining(), 55)

    def test_invalid_get_years_since_joined(self):
        self.assertNotEqual(self.avenger.years_since_joining(), -1)

    def test_valid_get_notes(self):
        self.assertEqual(self.avenger.notes(),
                         'Merged with Ultron in Rage of Ultron Vol. '
                         '1. A funeral was held.')

    def test_invalid_get_notes(self):
        self.assertNotEqual(self.avenger.notes(),
                            'Unmatched string')

    def test_valid_get_str(self):
        self.assertEqual(self.avenger.__str__(),
                         'Henry Jonathan "Hank" Pym')

    def test_invalid_get_str(self):
        self.assertNotEqual(self.avenger.__str__(),
                            'unmatching string')

    def test_valid_get_repr(self):
        self.assertEqual(self.avenger.__repr__(),
                         'Avenger(name_alias=Henry Jonathan "Hank" Pym,'
                         'url=http://marvel.wikia.com/Henry_Pym_(Earth-616))')

    def test_invalid_get_repr(self):
        self.assertNotEqual(self.avenger.__repr__(),
                            'Avenger(name_alias=Nonmatching name,url=badurl)')


if __name__ == '__main__':
    unittest.main()
