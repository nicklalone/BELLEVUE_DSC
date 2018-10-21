import sys
import csv


# need two blank lines between, functions should be all lower case
def argumentexists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


# need two blank lines between, functions should be all lower case
def readrows(inputCSV):
    with open (inputCSV,'r') as read:
        listOfOrderedDics = []
        readCSV = csv.fieldnames
        for row in readCSV:
            listOfOrderedDics.append(row)
        for key in readCSV: # keys was undefined, changed to readCSV
            print(key, listOfOrderedDics[160][key], end=" ")


if __name__ == "__main__":
    csvToRead = argumentexists(1)
    readrows(csvToRead)
# having a little trouble with this one
