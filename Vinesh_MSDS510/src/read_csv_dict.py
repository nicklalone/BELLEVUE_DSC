import csv
import sys
from pprint import pprint

def main():
    with open(sys.argv[1], newline='') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]
        print('Printing header')
        pprint(fieldnames)
        print('Printing 161th record ')
        pprint(records[161])



if __name__ == '__main__':
    main()
