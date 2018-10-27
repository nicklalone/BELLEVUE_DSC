import sys
import csv
# Python 3 uses dot notation to specify a sub-directory, then a file, and you import
# a class within the file.
#Here, at first I tried from src.msds510.avenger and was wondering why my code wouldn't work.  it wasn't until I changed it to msds510 that it worked.
from msds510.avenger import Avenger

def main():
    """
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
    """
        Reads an infile, sorts the content, and
        sends the sorted records and an outfile
        destination to printMarkdown to print
        Args:
            infile: a file location to read data from
            outfile: a destination file location
        Result:
            executes the printMarkdown function with
            sorted records and an outfile to write
            the results to.
    """

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file,
                           key=lambda k: int(k['appearances']),
                           reverse=True)[:10]

    avenger = Avenger()
    avenger.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
