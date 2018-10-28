import unittest
from msds510.utils import conversion


class ConversionTest(unittest.TestCase):

    def setUp(self):
        self.dict_example = {'a': 1, 'b': 52, 'd': 6}
        self.list_example = ['a', 'c', 'd']
        self.list_names = ['FirstName!!', 'Second Name\n', 'Third   Name\n']
        self.field_values = [{
            'appearances': '10',
            'current': 'YES',
            'year': '1980',
            'notes': 'these are some notes!',
            'month_joinded': 'sep',
            'full_reserve_avengers_intro': 'Sep-80',
            }
        ]

        self.field_value = {
            'appearances': '10',
            'current': 'YES',
            'year': '1980',
            'notes': 'these are some notes!',
            'month_joinded': 'sep',
            'full_reserve_avengers_intro': 'Sep-80',
        }

        self.notes = 'These are some notes with ' \
                     'a space and a carriage return \n'

    def test_float_str(self):
        self.assertEqual(conversion.to_int('2.9'), None)

    def test_float(self):
        self.assertEqual(conversion.to_int(2.9), 2)

    def test_invalid_str(self):
        self.assertEqual(conversion.to_int('invalid string'), None)

    def test_int_input(self):
        self.assertEqual(conversion.to_int('4'), 4)

    def test_valid_list_tuple_input1(self):
        self.assertEqual(conversion.get_value(self.list_example, 'q'), None)

    def test_valid_list_tuple_input2(self):
        self.assertEqual(conversion.get_value(self.list_example, 'd'), 2)

    def test_valid_dict_input1(self):
        self.assertEqual(conversion.get_value(self.dict_example, 'a'), 1)

    def test_valid_dict_input2(self):
        self.assertEqual(conversion.get_value(self.dict_example, 'b'), 52)

    def test_dict_missing_key(self):
        self.assertEqual(conversion.get_value(self.dict_example, 'x'), None)

    def test_valid_to_bool(self):
        self.assertEqual(conversion.to_bool("YES"), True)

    def test_valid_to_bool2(self):
        self.assertEqual(conversion.to_bool("NO"), False)

    def test_valid_to_bool3(self):
        self.assertEqual(conversion.to_bool(""), None)

    def test_invalid_to_bool(self):
        self.assertNotEqual(conversion.to_bool("YES"), False)

    def test_valid_make_nice_name(self):
        self.assertEqual(conversion.make_nice_name(self.list_names[0]),
                         'firstname')

    def test_valid_make_nice_name2(self):
        self.assertEqual(conversion.make_nice_name(self.list_names[1]),
                         'second_name')

    def test_valid_clean_notes(self):
        self.assertEqual(conversion.clean_notes(self.notes),
                         'These are some notes with a '
                         'space and a carriage return')

    def test_invalid_clean_notes(self):
        self.assertNotEqual(conversion.clean_notes(self.notes),
                            'These are some notes with a '
                            'space and a carriage return \n')

    def test_valid_clean_field_names(self):
        self.assertEqual(conversion.clean_field_names(self.field_values),
                         [
                             {'appearances': 10,
                              'current': True,
                              'full_reserve_avengers_intro': 'Sep-80',
                              'month_joinded': 9,
                              'notes': 'these are some notes!',
                              'year': 1980,
                              'years_since_joining': 38
                              }
                         ])

    def test_invalid_clean_field_names(self):
        self.assertNotEqual(conversion.clean_field_names(
            self.field_values),
            [
                 {'appearances': 100,
                  'current': False,
                  'full_reserve_avengers_intro': 'Sep-90',
                  'month_joinded': 10,
                  'notes': 'these are some notesX',
                  'year': 1983,
                  'years_since_joining': 444
                  }
            ]
        )

    def test_valid_transform_records(self):
        self.assertEqual(conversion.transform_record(
            self.field_value),
             {'appearances': 10,
              'current': True,
              'full_reserve_avengers_intro': 'Sep-80',
              'month_joinded': 9,
              'notes': 'these are some notes!',
              'year': 1980,
              'years_since_joining': 38
              }

        )

    def test_invalid_transform_records(self):
        self.assertNotEqual(conversion.transform_record(
            self.field_value),
             {'appearances': 100,
              'current': False,
              'full_reserve_avengers_intro': 'Sep-90',
              'month_joinded': 10,
              'notes': 'these are some notesX',
              'year': 1983,
              'years_since_joining': 444
              }
        )


if __name__ == '__main__':
    unittest.main()
