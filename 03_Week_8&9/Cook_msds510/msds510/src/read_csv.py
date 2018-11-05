import sys
import csv
from pprint import pprint

# The following code uses CSV reader and generates a CSV reader object
# The CSV reader object is further iterated to get all the rows

def read_csv(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.reader(f)
        rows = [row for row in csv_reader]

    print('Printing Row 162 using csv.reader')
    pprint(rows[162])

# The following code uses a dict reader and generates a dictionary reader object
# The dictionary reader is iterated to get the rows
# The Advantage with the dictionary reader is that we can extract fieldnames from the dictionary object

def read_csv_dict(csv_path):
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    print('Printing record 161 using csv.DictReader')
    pprint(records[161])
    print('Printing fieldnames')
    pprint(fieldnames)

# The following takes in each of the fieldnames extracted and performs the following methods to make python friendly names

    for name in fieldnames:
        nice_name = name.lower().replace(' ', '_').replace('/', '_').replace('?', '')
        print("'{}', ".format(nice_name))

#  The following code takes in file name as arguement and if the file name is not entered it will give out a message

def main():
    args = sys.argv

    if len(args) < 2:
        print('usage: read_csv <input_csv>')
    else:
        read_csv(args[1])
        read_csv_dict(args[1])


if __name__ == '__main__':
    main()
