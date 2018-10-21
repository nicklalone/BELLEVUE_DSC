import sys
import csv
from pprint import pprint

<<<<<<< HEAD

# need two blank lines between, functions should be all lower case
def argumentexists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]
=======
>>>>>>> eefa1e681afad7ee45e9467b2d9da4002536b14a

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

<<<<<<< HEAD
# need two blank lines between, functions should be all lower case
def readrows(inputCSV):
    with open (inputCSV,'r') as read:
        listOfOrderedDics = []
        readCSV = csv.fieldnames
        for row in readCSV:
            listOfOrderedDics.append(row)
        for key in readCSV: # keys was undefined, changed to readCSV
            print(key, listOfOrderedDics[160][key], end=" ")
=======
>>>>>>> eefa1e681afad7ee45e9467b2d9da4002536b14a


if __name__ == "__main__":
<<<<<<< HEAD
    csvToRead = argumentexists(1)
    readrows(csvToRead)
# having a little trouble with this one
=======
      main()
>>>>>>> eefa1e681afad7ee45e9467b2d9da4002536b14a
