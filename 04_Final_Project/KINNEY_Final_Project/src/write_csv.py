"""
c. Write CSV with DictWriter
Implement the write_csv.py script. It should take two arguments as input, the input CSV file, and the output CSV file.
When completed, you should be able to run the script as follows.

python write_csv.py ..\data\interim\inputfile_utf8.csv ..\data\processed\outputfile.csv

Use csv.DictReader to read in the data from the input CSV like you did in the previous step. Make sure you get the
original fieldnames from the input file. Change those fieldnames to Python friendly names and use those as your new
fieldnames when you use DictWriter to write your new CSV file.

Implementation hints
1. Remember to change the fieldnames in your dictionary records to match the fieldnames in your output CSV
2. Don't forget to write the header to your new output CSV
"""

import csv
import sys


def make_nice_name(name):
    """
    :param name:
    :return name:
    Takes in a name as an argument and returns a Python-friendly name that follows the following rules.
        1. Remove question marks
        2. Strip trailing newline characters
        3. Replace spaces and slashes with the underscore character
        4. Convert to all lower case letters
    """
    name = name.rstrip("?").rstrip("\n")
    name = name.replace("/", "_").replace(" ", "_").lower()
    return name


def write_csv_dict(file_to_read, file_to_write):
    dictfile = open(file_to_read, newline='', encoding='utf-8')
    dictreader = csv.DictReader(dictfile)
    nice_fields = []
    headers = dictreader.fieldnames
    for i in range(len(headers)):
        name = make_nice_name(headers[i])
        nice_fields.append(name)
    dictreader.fieldnames = nice_fields

    writefile = open(file_to_write, 'w', newline='', encoding='utf-8')
    writer = csv.DictWriter(writefile, fieldnames=nice_fields)
    writer.writeheader()
    writer.writerows(dictreader)
    writefile.close()
    print('File {0} created and copied to processed folder.'.format(file_to_write))

    return


def main():
    write_csv_dict(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
