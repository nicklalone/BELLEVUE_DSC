import sys
import csv

def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv [index]

def readRows(inputCSV):
    with open (inputCSV, 'r') as read:
        listOfOrderedDics =[]
        readCSV = csv.DictReader(read)
        keys=readCSV.DictReader(read)  # Hsu-Comment: This line is extraneous since the "keys" variable is redefined in the next line.
        keys = readCSV.fieldnames
        for row in readCSV:
            listOfOrderedDics.append(row)
        for key in keys:
            print(key, listOfOrderedDics[160][key], end = " ")

if __name__=="__main__":
                    csvToRead = argumentExists(1)
                    readRows (csvToRead)

