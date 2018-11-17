import sys
import csv
from msds510.utils import conversion
from msds510 import util
import re

"""
Execution: python process_csv.py ../data/interim/marvel-wikia-data_utf8.csv ../data/processed/marvel-wikia-data_processed.csv
"""


def processfile(infile, outfile):
    """
    Function to read infile, cleans the records and writes to csv using writeCSVFile to an outfile.
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the writeCSVFile with python
        friendly content and an outfile to write
        the results to.
    :return: none
    """

    file = []
    fieldnames = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    with open(infile, 'r') as csvfile1:
        fieldreader = csv.reader(csvfile1, delimiter=',')
        fielddata = list(fieldreader)[0]
        header = reader.fieldnames
        new_header = []
        for item in header:
            # I like your usage of Regular expression in the following code
            new_header.append(re.sub(r'[^0-9a-z_\_]', '', item.replace(" ", "_").replace("/", "_").strip("?").strip().lower()))
        new_header.append("days_since_first_appearance")

    file = conversion.clean(file)

    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_header, lineterminator='\n')
        writer.writeheader()
        i = 0
        for d in file:
            # if i < 1: print(type(d))
            # i += 1
            writer.writerow(d)

        print("Marvel csv - %s processed and placed in the %s directory" % (util.getfilename(outfile), util.getfilepath(outfile)))


def main():
    """
    Main function to interpret command line request
    Args: array with input and output files
    :return: none
    """
    if len(sys.argv) != 3:
        print("This converter takes two parameters, an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        processfile(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
