import sys
import csv
from msds510.fandango import Fandango as fd


def main():
    """interprets command line request
    Args:
        argv: an array with input and output files

    Returns:
        no return. Executed generateReport with
        collected file names.
    """
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file, key=lambda k: int(k['fandango_votes']), reverse=True)[:10]

    fan_record = fd()
    fan_record.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
