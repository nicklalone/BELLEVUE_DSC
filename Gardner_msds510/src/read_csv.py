import sys
import csv


def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


rows = []
def readRows(inputCSV):
    with open(inputCSV, 'r') as read:
        readCSV = csv.reader(read)
        for row in readCSV:
            rows.append(row)
        print(rows[161])


if __name__ == '__main__':
    csvToRead = argumentExists(1)
    readRows(csvToRead)
