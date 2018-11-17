import unittest
from msds510.democrat_bench import DemocraticBench

class DemocratTest(unittest.TestCase):

    def setUp(self):
        self.pym_record = {
            'cand': 'Andrew Neel',
            'raised_exp': '12345',
            'raised_act': '54321',
        }

        self.democrat_bench = DemocraticBench(self.pym_record)

    def test_valid_get_candidate(self):
        self.assertEqual(self.democrat_bench.candidate(),
                         'Andrew Neel')

    def test_invalid_get_candidate(self):
        self.assertNotEqual(self.democrat_bench.candidate(),
                            'Other Name')

    def test_valid_raised_exp(self):
        self.assertEqual(self.democrat_bench.raised_exp(),
                         '12345')

    def test_invalid_raised_exp(self):
        self.assertNotEqual(self.democrat_bench.raised_exp(),
                            '123')

    def test_valid_get_raised_act(self):
        self.assertEqual(self.democrat_bench.raised_act(),
                         '54321')

    def test_invalid_get_raised_act(self):
        self.assertNotEqual(self.democrat_bench.raised_act(),
                            '111')

if __name__ == '__main__':
    unittest.main()
