import sys
import csv


def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


def readRows(inputCSV):
    with open(inputCSV, 'r') as read:
        listoforderedDics = []
        readCSV = csv.DictReader(read)
        keys = readCSV.fieldnames
        for row in readCSV:
            listoforderedDics.append(row)
        for key in keys:
            print(key, listoforderedDics[160][key], end=" ")


if __name__ == '__main__':
    csvToRead = argumentExists(1)
    readRows(csvToRead)
