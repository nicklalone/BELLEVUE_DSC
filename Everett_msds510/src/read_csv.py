import sys
import csv
from pprint import pprint


#Reads a .csv file and enters each row of the .csv file into a list. Reads each row of the .csv file using the csv.reader() function.
def read_csv(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]

    print('Printing Row 162 using csv.reader')
    pprint(rows[162])


# Reads a .csv file and enters each row of the .csv file into a dictionary record. Reads each row of the .csv file using the csv.DictReader() function.
def read_csv_dict(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    # printing off the 161st record per assignment directions
    print('Printing record 161 using csv.DictReader')
    pprint(records[161])
    print('Printing fieldnames')
    pprint(fieldnames)

    # Cleaning up the fieldnames to make them more Python acceptable.
    for name in fieldnames:
        nice_name = name.lower().replace(' ', '_').replace('/', '_').replace('?', '')
        print("'{}', ".format(nice_name))


def main():
    args = sys.argv

    if len(args) < 2:
        print('usage: read_csv <input_csv>')
    else:
        read_csv(args[1])
        read_csv_dict(args[1])


if __name__ == '__main__':
    main()
