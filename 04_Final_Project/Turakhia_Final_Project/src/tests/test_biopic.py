import unittest
import datetime
from msds510.biopic import Biopic


class BiopicTest(unittest.TestCase):

    def setUp(self):
        self.pym_record = {
			'title':'10 Rillington Place',
            'box_office': '-',
            'year_release': '1971',
            'director': 'Richard Fleischer',
            'site': 'http://www.imdb.com/title/tt0066730/',
            'lead_actor_actress': 'Richard Attenborough',
        }

        self.biopic = Biopic(self.bio_record)

    def test_valid_get_title(self):
        self.assertEqual(self.biopic.title(), '10 Rillington Place')

    def test_invalid_get_name_alias(self):
        self.assertNotEqual(self.biopic.title(),
                            'Other Name')

    def test_valid_get_site(self):
        self.assertEqual(self.biopic.site,
                         'http://www.imdb.com/title/tt0066730/')

    def test_invalid_get_site(self):
        self.assertNotEqual(self.biopic.site(),
                            'not url string')
    def test_valid_get_year_release(self):
        self.assertEqual(self.biopic.year_release(), 1971)

    def test_invalid_get_year_release(self):
        self.assertNotEqual(self.biopic.year_release(),
                            "not a match")
							
    def test_valid_get_box_office(self):
        self.assertEqual(self.biopic.box_office(), '-')

    def test_invalid_get_box_office(self):
        self.assertNotEqual(self.biopic.box_office(), '12M')

    def test_valid_get_director(self):
        self.assertEqual(self.biopic.director(), 'Richard Fleischer')

    def test_invalid_get_director(self):
        self.assertNotEqual(self.biopic.director(), 'No Name')


    def test_valid_get_lead_actor_actress(self):
        self.assertEqual(self.biopic.lead_actor_actress(), 'Richard Attenborough')

    def test_invalid_get_lead_actor_actress(self):
        self.assertNotEqual(self.biopic.lead_actor_actress(), 'Allen')

    def test_valid_get_str(self):
        self.assertEqual(self.biopic.__str__(),
                         '10 Rillington Place" Pym')

    def test_invalid_get_str(self):
        self.assertNotEqual(self.biopic.__str__(),
                            'unmatching string')

    def test_valid_get_repr(self):
        self.assertEqual(self.biopic.__repr__(),
                         'Biopic(name_alias=10 Rillington Place'
                         'site=http://www.imdb.com/title/tt0066730/')

    def test_invalid_get_repr(self):
        self.assertNotEqual(self.biopic.__repr__(),
                            'Biopic(name_alias=Nonmatching name,site=badurl)')


if __name__ == '__main__':
    unittest.main()
