#this module is to read in the Avengers csv file using the csv reader
#it also uses the dictionary reader and
#changes the field names to Python friendly names

import sys
import csv
from pprint import pprint


def read_csv(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]

    print('Printing Row 162 using csv.reader')
    pprint(rows[162])


def read_csv_dict(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    print('Printing record 161 using csv.DictReader')
    pprint(records[161])
    print('Printing fieldnames')
    pprint(fieldnames)

    for name in fieldnames:
        nice_name = name.lower().replace(' ', '_').replace('/', '_').replace('?', '')
        print("'{}', ".format(nice_name))

# Check to see if the command line interface has at least 2 arguments entered
def main():
    args = sys.argv

    if len(args) < 2:
        print('usage: read_csv <input_csv>')
    else:
        read_csv(args[1])
        read_csv_dict(args[1])


if __name__ == '__main__':
    main()
