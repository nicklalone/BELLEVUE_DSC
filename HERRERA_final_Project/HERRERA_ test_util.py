import datetime
import unittest
import util

class TestUtilFunctions(unittest.TestCase):

    '''
    Unit tests for to_int function
    '''

    def test_int_str(self):
        self.assertEqual(util.to_int('2'),2)

    def test_float_str(self):
        self.assertEqual(util.to_int('3.14'),3)

    def test_invalid_str(self):
        self.assertEqual(util.to_int('hello'),None)

    def test_int_input(self):
        self.assertEqual(util.to_int(5),5)

    '''
    Unit tests for get_value function
    '''

    def test_valid_dict_input(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        self.assertEqual(util.get_value(x,'a'),1)
        self.assertEqual(util.get_value(x,'b'),52)
        self.assertEqual(util.get_value(x,'d'),6)

    def test_dict_missing_key(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        self.assertEqual(util.get_value(x,'q'),None)
    
    def test_valid_list_input(self):
        y = ['a', 'c', 'd']
        self.assertEqual(util.get_value(y,'a'),0)
        self.assertEqual(util.get_value(y,'c'),1)
        self.assertEqual(util.get_value(y,'d'),2)

    def test_list_missing_key(self):
        y = ['a', 'c', 'd']
        self.assertEqual(util.get_value(y,'b'),None)

    '''
    Unit tests for get_date_joined function
    '''

    def test_valid_year(self):
        self.assertEqual(util.get_date_joined('1988','Jun-88'),datetime.date(1988,6,1))

    def test_invalid_year(self):
        self.assertEqual(util.get_date_joined('hello','Jun-88'),None)

    def test_valid_month(self):
        self.assertEqual(util.get_date_joined('2013','13-Nov'),datetime.date(2013,11,1))

    def test_invalid_month(self):
        self.assertEqual(util.get_date_joined('2013','hello'),None)

if __name__ == '__main__':
    unittest.main()
