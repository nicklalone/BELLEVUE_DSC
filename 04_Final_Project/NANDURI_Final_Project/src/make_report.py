import sys
import csv
from msds510.marvel import Marvel
from msds510 import util

"""
Execution: python make_report.py ../data/processed/marvel-wikia-data_processed.csv ../reports/top_ten_marvel_appearances.md
"""


def zero_app(appearances):
    if len(appearances) == 0:
        return 0
    else:
        return int(appearances)


def generatereport(infile, outfile):
    """
    Function to read an infile, generates the top 10 appearances report using printMarkdown
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the printMarkdown function with
        sorted records and an outfile to write
        the results to.
    :return: none
    """

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file,
                           key=lambda k: zero_app(k['appearances']),
                           reverse=True)[:10]

    marvel = Marvel()
    marvel.to_markdown(sortedRecords, outfile)
    print("Report %s generated and placed in the %s directory" % (util.getfilename(outfile) , util.getfilepath(outfile)))


def main():
    """
    Main function to interpret command line request
    Args: an array with input and output files
    :return: none
    """
    if len(sys.argv) != 3:
        print("This report generator takes two parameters, an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generatereport(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()

