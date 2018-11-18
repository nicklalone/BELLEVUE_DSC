import sys
import csv
from pprint import pprint

# The code below takes the path for the input file  and reads the file using csv reader
# csv reader gives a csv_reader object
# The reader object was iterated to print the required rows

def read_csv(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]
    
    #Joe F.: Looks like you're printing row 62; are one of these a typo?
    print('Printing Row 162 using csv.reader')
    pprint(rows[62])

# The following code takes the path for the input file
# csv_DictReader gives a csv_dictreader object
# The dictionary reader iterated to print the rows
# Dictreader knows that the first row corresponds to filed names

def read_csv_dict(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    print('Printing record 161 using csv.DictReader')
    pprint(records[61])
    print('Printing fieldnames')
    pprint(fieldnames)

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
