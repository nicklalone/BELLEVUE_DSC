import sys
import csv
from pprint import pprint


# The following code takes the path for the input file
# csv_DictReader gives a csv_dictreader object
# The dictionary reader iterated to print the rows
# Dictreader knows that the first row corresponds to filed names

def csvdict_read(inputfilepath):
    with open(inputfilepath) as f:
        csv_dictreader = csv.DictReader(f)
        fieldnames = csv_dictreader.fieldnames
        rows = [row for row in csv_dictreader]
        pprint(rows[161])

# The code below is to check if there is atleast 2 arguements entered in the command line interface

def main():
    args = sys.argv

    if len(args) < 1:
        print("Please enter the path name for the two files")
    else:
        csvdict_read(args[1])


if __name__ == "__main__":
      main()
