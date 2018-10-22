import csv
import sys

"""
This module helps to convert create a new CSV file with clean header name.
command line argument 1 is csv file containing initial header names
command line argument 2 is name of the csv file which will be created with new header names

"""

def main():
    with open(sys.argv[1], newline='') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        fieldnames = csv_reader.fieldnames
        clean_fieldnames = [clean_name(name) for name in fieldnames]
        records = [row for row in csv_reader]
        clean_records = [{clean_name(name): value for name, value in record.items()} for record in records]

        with open(sys.argv[2], 'w') as g:
            csv_dic_writer = csv.DictWriter(g, fieldnames=clean_fieldnames)
            csv_dic_writer.writeheader()
            csv_dic_writer.writerows(clean_records)


def clean_name(name):
    return name.lower().replace('?', '').replace('/', '_').replace(' ', '_')


if __name__ == '__main__':
    main()
