import unittest
from tests import test_democratic_bench, test_util_conversion


def main():
    """interprets command line request
    Args:
        argv: received but unused

    Result:
        Executed runTests which runs unit tests.
    """
    runTests()


def runTests():
    """runs all test cases.
    Result:
        Executed runTests which runs unit tests.
    """

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        test_util_conversion.ConversionTest
    )
    unittest.TextTestRunner().run(suite)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        test_democratic_bench.DemocratTest
    )
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
