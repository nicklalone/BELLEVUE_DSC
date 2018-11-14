import sys
import csv
from msds510.utils import conversion


def main():
    """interprets command line request
    Args:
        argv: an array with input and output files

    Result:
        Executed processFile with collected file names.
    """
    if (len(sys.argv) != 3):
        print("this converter takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        processFile(sys.argv[1], sys.argv[2])


def processFile(infile, outfile):
    """reads an infile, cleans the fieldnames for
    both the header and the corresponding field
    titles by row and then sends it to writeCSVFile
    to be writted to an outfile.
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the writeCSVFile with python
        friendly content and an outfile to write
        the results to.
    """

    file = []
    fieldnames = []
    with open(infile, 'rU') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    with open(infile, 'rU') as csvfile1:
        fieldreader = csv.reader(csvfile1, delimiter=',')
        fielddata = list(fieldreader)[0]
        fieldnames = [conversion.make_nice_name(field) for field in fielddata]

    file = conversion.clean_field_names(file)


    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                lineterminator='\n')
        writer.writeheader()
        for d in file:
            writer.writerow(d)


if __name__ == '__main__':
    main()
