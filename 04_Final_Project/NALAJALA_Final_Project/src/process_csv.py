import sys
import csv
from msds510 import util

#Command:python process_csv.py ../data/raw/biopics.csv ../data/processed/biopics_processed.csv

def main(input_file_path, output_file_path):
    """
    Converts csv file from 'ISO-8859-1' to 'utf-8'
    @param input_file_path:Command line argument
    @param output_file_path:Command line argument
    """
    try:
        file_content = []
        input_file_header = []
        with open(input_file_path, 'r', encoding='ISO-8859-1') as source_file:
            input_file_content = csv.DictReader(source_file)
            input_file_header = input_file_content.fieldnames
            input_file_header.append('years_since_released')
            file_content = list(input_file_content)

        input_file_header = util.update_header(input_file_header)

        with open(output_file_path, 'w', encoding='UTF8', newline='') as target_file:
            output_file_content = csv.DictWriter(target_file, input_file_header)
            output_file_content.writeheader()
            for input_file_row in file_content:
                output_file_row = {util.python_friendly_name(key): value for key, value in input_file_row.items()}
                output_file_content.writerow(util.transform_record(output_file_row))

        print("File processed and copied to {}".format(output_file_path))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except BaseException as e:
        print("Error during processing")
        print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


if __name__ == '__main__':
    if util.verify_arguments(sys.argv):
        main(sys.argv[1], sys.argv[2])