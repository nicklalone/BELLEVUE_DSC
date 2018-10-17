import csv
import sys
from pprint import pprint


def read_csv_dict(input_file, row_to_print):
    try:
        with open(input_file) as file:
            csv_reader = csv.DictReader(file)
            fieldnames = csv_reader.fieldnames
            records = [row for row in csv_reader]

        print('Print the row using csv.DictReader...\n')
        pprint(records[row_to_print])
        print('Printing the headers...\n')
        pprint(fieldnames)

        print('Printing the formatted headers now...')
        for name in fieldnames:
            nice_name = name.lower().replace(' ', '_').replace('/', '_').replace('?', '')
            print("'{}', ".format(nice_name))

    except:
        print('An exception occurred:', sys.exc_info())
