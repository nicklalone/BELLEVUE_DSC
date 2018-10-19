# uses the csv module to read the csv as a CSV
import csv
import sys
from pprint import pprint
import read_csv_dict


def read_csv(input_file):
    # add error handling
    try:
        with open(input_file) as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]
        print("Print the 162nd row...")
        pprint(rows[162])

    except:
        print('An exception occurred:', sys.exc_info())

def main():
    args = sys.argv
    if len(args) < 3:
        print('Usage: read_csv <input file> <row to print>')
    else:
        read_csv(args[1])
        read_csv_dict.read_csv_dict(args[1], int(args[2]))

if __name__ == '__main__':
    main()
