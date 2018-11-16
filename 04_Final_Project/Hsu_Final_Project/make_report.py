import sys
import csv
from utils.avenger import Avenger


def main():
    # Executes generate_report function with the 2 arguments
    # 2 arguments: input file and output file location
    if len(sys.argv) != 3:
        print("This report generator takes two parameters, an input file and an output file.")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generate_report(sys.argv[1], sys.argv[2])


def generate_report(infile, outfile):
    # Reads an input file and sorts it to display the top 10.
    # Generates a report for the top 10 names with the smallest gender percentage gap.
    # Output file name should be a markdown file as the Avenger class is formatted as such.

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)
    sorted_records = sorted(file, key=lambda x: x['gap'])[:10]
    avenger = Avenger()
    avenger.to_markdown(sorted_records, outfile)


if __name__ == '__main__':
    main()
