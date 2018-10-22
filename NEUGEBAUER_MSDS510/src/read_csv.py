# uses the csv module to read the csv as a CSV
import csv
import sys
from pprint import pprint
import read_csv_dict


def read_csv(input_file):
    # add error handling
    try:
        with open(input_file) as file:
            csv_reader = csv.reader(file)
            rows = [row for row in csv_reader]
        print("Print the 162nd row...")
        pprint(rows[162])  #Remember that Python starts at 0, so it might not be entirely true that you are printing the 162nd row? -Myrna

    except:
        print('An exception occurred:', sys.exc_info())

def main():
    args = sys.argv
    if len(args) < 3:  # Did you mean to use ">" instead of "<"?
        print('Usage: read_csv <input file> <row to print>')
    else:  # This will only run if there are 3 or more arguments but the assignment is only using 2 (including "Python" itself).
        read_csv(args[1])
        read_csv_dict.read_csv_dict(args[1], int(args[2]))

if __name__ == '__main__':
    main()
# Expanding on my earlier comment, if you enter "python read_csv.py ../data/interim/avengers_utf8.csv" in the command prompt, the output is the print statement. So the "read_csv" function will not be run.
# I do like the additional functionality of entering in a desired row as an output but you also have "read_csv_dict.py" which this is using so this script is slightly more complicated than it should be.
# Also, every time this script is run, the 162nd row is printed every time so it is extra work if you want the main functionality of the script to be inputting the desired row.
# Going further though, I would suggest a slightly different way than doing a row number input since it would require knowing which row number you would want to display instead of something like the Avenger's name.
