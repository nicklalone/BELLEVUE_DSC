import datetime
from unicodedata import decimal


class DemocraticBench:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.candidate = record["cand"]
            self.raised_expected = record["raised_exp"]
            self.raised_actual = record["raised_act"]

    def candidate(self):
        """

        Returns:
            str: The name of the candidate raising money

        """
        return self.candidate

    def raised_expected(self):
        """

        Returns:
            decimal: Expected amount of money that candidate wanted to raise

        """
        return decimal(self.raised_expected)

    def raised_actual(self):
        """

        Returns:
            decimal: Actual amount of money that candidate raised

        """
        return decimal(self.raised_actual)

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of top 10 candidate records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """

        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                democrat_bench = DemocraticBench(rc)
                ofile.write("# " + str(idx + 1) + ". "

                            + democrat_bench.candidate + "\n\n")

                ofile.write("* Expected Money to be Raised: $"

                            + str(democrat_bench.raised_expected + "\n"))

                ofile.write("* Money Actually Raised: $" + str(democrat_bench.raised_actual) + "\n\n")
