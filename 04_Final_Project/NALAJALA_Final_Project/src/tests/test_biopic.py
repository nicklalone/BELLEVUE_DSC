import unittest
from msds510.biopic import Biopic



class BiopicTest(unittest.TestCase):

    def setUp(self):
        self.bp_record = {
            'title': 'A Beautiful Mind',
            'site': 'http://www.imdb.com/title/tt0268978/',
            'country': 'US',
            'year_release': '2001',
            'box_office': '171',
            'director': 'Ron Howard',
            'number_of_subjects': '1',
            'subject': 'John Nash',
            'type_of_subject': 'Academic',
            'race_known': 'FALSE',
            'subject_race': '',
            'person_of_color': 'FALSE',
            'subject_sex': 'Male',
            'lead_actor_actress': 'Russell Crowe',
            'years_since_released': '17'
        }

        self.biopic = Biopic(self.bp_record)

    def test_valid_get_title(self):
        self.assertEquals(self.biopic.title(),'A Beautiful Mind')

    def test_invalid_get_title(self):
        self.assertNotEqual(self.biopic.title(), 'A Beautiful poetry')

    def test_valid_get_site(self):
        self.assertEquals(self.biopic.site(),'http://www.imdb.com/title/tt0268978/')

    def test_invalid_get_site(self):
        self.assertNotEqual(self.biopic.site(), 'http://www.imdb.com/title//')

    def test_valid_get_country(self):
        self.assertEquals(self.biopic.get_country(),'US')

    def test_invalid_get_country(self):
        self.assertNotEqual(self.biopic.get_country(), 'UK')

    def test_valid_get_year_release(self):
        self.assertEquals(self.biopic.year_release(),2001)

    def test_invalid_get_year_release(self):
        self.assertNotEqual(self.biopic.year_release(), 2011)

    def test_valid_get_box_office(self):
        self.assertEquals(self.biopic.box_office(),171.00)

    def test_invalid_get_box_office(self):
        self.assertNotEqual(self.biopic.box_office(), 2011.00)

    def test_valid_get_get_director(self):
        self.assertEquals(self.biopic.get_director(), 'Ron Howard')

    def test_invalid_get_get_director(self):
        self.assertNotEqual(self.biopic.get_director(), 'Howard Ron')

    def test_valid_get_number_of_subjects(self):
        self.assertEquals(self.biopic.get_number_of_subjects(),1)

    def test_invalid_get_number_of_subjects(self):
        self.assertNotEqual(self.biopic.get_number_of_subjects(), 2)

    def test_valid_get_subject(self):
        self.assertEquals(self.biopic.get_subject(),'John Nash')

    def test_invalid_get_subject(self):
        self.assertNotEqual(self.biopic.get_subject(), 'Nash')

    def test_valid_get_type_of_subject(self):
        self.assertEquals(self.biopic.get_type_of_subject(),'Academic')

    def test_invalid_get_type_of_subject(self):
        self.assertNotEqual(self.biopic.get_type_of_subject(), 'Non Academic')

    def test_valid_get_is_race_known(self):
        self.assertEquals(self.biopic.is_race_known(),False)

    def test_invalid_get_is_race_known(self):
        self.assertNotEqual(self.biopic.is_race_known(), True)

    def test_valid_get_subject_race(self):
        self.assertEquals(self.biopic.get_subject_race(),'')

    def test_invalid_get_subject_race(self):
        self.assertNotEqual(self.biopic.get_subject_race(), 'race')

    def test_valid_get_person_of_color(self):
        self.assertEquals(self.biopic.get_person_of_color(),False)

    def test_invalid_get_person_of_color(self):
        self.assertNotEqual(self.biopic.get_person_of_color(), True)

    def test_valid_get_lead_actor_actress(self):
        self.assertEquals(self.biopic.get_lead_actor_actress(),'Russell Crowe')

    def test_invalid_get_lead_actor_actress(self):
        self.assertNotEqual(self.biopic.get_lead_actor_actress(), 'Russell')

    def test_valid_get_years_since_released(self):
        self.assertEquals(self.biopic.years_since_released(),17)

    def test_invalid_get_years_since_released(self):
        self.assertNotEqual(self.biopic.years_since_released(), 45)

    def test_valid_get_str(self):
        self.assertEqual(self.biopic.__str__(),
                         'A Beautiful Mind')

    def test_invalid_get_str(self):
        self.assertNotEqual(self.biopic.__str__(),
                            'A Beautiful Person')

    def test_valid_get_repr(self):
        self.assertEqual(self.biopic.__repr__(),
                         'Biopic(title=A Beautiful Mind,'
                         'site=http://www.imdb.com/title/tt0268978/)')

    def test_invalid_get_repr(self):
        self.assertNotEqual(self.biopic.__repr__(),
                            'Biopic(title=wrong title name,url=wrong url)')

if __name__ == '__main__':
    unittest.main()
