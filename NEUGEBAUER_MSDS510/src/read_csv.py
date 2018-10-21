# uses the csv module to read the csv as a CSV
import csv
import sys
from pprint import pprint

import read_csv_dict


def read_csv(input_file):
    try:
        with open(input_file) as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]
        print("Print the 162nd row...")
        pprint(rows[162])  # Hsu-Comment: Depending on what the assignment means by "162nd row" but remember that Python indices start at 0.

    except:
        print('An exception occurred:', sys.exc_info())

def main():
    args = sys.argv
    if len(args) < 3:
        print('Usage: read_csv <input file> <row to print>')
    else:
        read_csv(args[1])
        read_csv_dict.read_csv_dict(args[1], int(args[2]))

if __name__ == '__main__':
    main()
# Hsu-Comments:
# If you enter "python read_csv.py ../data/interim/avengers_utf8.csv" in the command prompt, the output is the print statement. So the "read_csv" function will not be run.
# I do like the additional functionality of entering in a desired row as an output but you also have "read_csv_dict.py" which this is using so this script is slightly more complicated than it should be.
# However, it requires "dummy" arguments to be entered in since "read_csv" is only using 1 argument and "read_csv_dict" is using 2.
# Also, every time this script is run, the 162nd row is printed every time so it is extra work if you want the main functionality of the script to be inputting the desired row.
# Going further though, I would suggest a slightly different way than doing a row number input since it would require knowing which row number you would want to display instead of something like the Avenger's name.