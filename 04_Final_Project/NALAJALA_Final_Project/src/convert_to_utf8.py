import sys
from msds510 import util


def main(input_file_path, output_file_path):
    """
    Converts csv file from 'ISO-8859-1' to 'utf-8'
    @param input_file_path:Command line argument
    @param output_file_path:Command line argument
    Command:python convert_to_utf8.py ../data/raw/biopics.csv ../data/interim/biopics_utf8.csv
    """
    try:
        with open(input_file_path, encoding='ISO-8859-1') as source_file:
            file_content = source_file.read()

        with open(output_file_path, 'w', encoding='UTF8') as target_file:
            target_file.write(file_content)

        print("File created with utf-8 encoded data and copied to {}".format(output_file_path))
    except BaseException as e:
        print(str(e))
        print("Error during conversion. Please try again")


if __name__ == '__main__':
    if util.verify_arguments(sys.argv):
        main(sys.argv[1], sys.argv[2])