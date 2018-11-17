import sys
import csv

from msds510.Fifa import Fifa 
# if the avenger utility is supposed to be imported here, how do I do that? Which utility?
def main():

    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


    def generateReport(infile, outfile):
        """reads an infile, sorts the content, and
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
                           key=lambda k: float(k['population_share']),
                           reverse=True)[:10]

    Fifa = Fifa()
    Fifa.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
