import unittest
from tests import test_biopic

#Command:python run_tests.py
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
        test_biopic.BiopicTest
    )
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()