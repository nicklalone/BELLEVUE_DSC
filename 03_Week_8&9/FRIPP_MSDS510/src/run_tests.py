import unittest
from tests import test_avenger, test_util_conversion, test_util_date


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
        test_util_date.DateTest
    )
    unittest.TextTestRunner().run(suite)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        test_util_conversion.ConversionTest
    )
    unittest.TextTestRunner().run(suite)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        test_avenger.AvengerTest
    )
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
