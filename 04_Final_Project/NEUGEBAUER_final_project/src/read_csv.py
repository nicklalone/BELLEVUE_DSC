# uses the csv module to read the csv as a CSV
import csv
import sys
from pprint import pprint
import read_write_csv_dict
import yaml

def read_csv(input_file, input_row_to_print):
    # add error handling
    try:
        with open(input_file) as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]

        print('Print row', input_row_to_print)
        pprint(rows[int(input_row_to_print)])
    except:
        print('An exception occurred:', sys.exc_info())

def main():
    try:
        config = yaml.safe_load(open('../config/config.yml'))
        interimUTF8Name = config.get('InterimUTF8File')
        rowToPrint = int(config.get('RowToPrint'))
        output_file = config.get('OutputFile')

        read_csv(interimUTF8Name, rowToPrint)
        read_write_csv_dict.read_write_csv_dict(interimUTF8Name, output_file)

        print('\nCompleted building the processed CSV file ', output_file)
    except:
        print('An exception occurred:', sys.exc_info())

if __name__ == '__main__':
    main()
