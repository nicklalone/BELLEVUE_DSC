import sys
import csv


def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


def fixHeader(headerToFix):
    corr_category = headerToFix
    corr_category = corr_category.lower()
    corr_category.strip('\n').strip('?').rstrip().lstrip()
    corr_category = corr_category.replace('/','_')
    return corr_category


def processedCSV(output, headers, input):
    with open(output, 'w', newline='') as written:
        dw = csv.DictWriter(written, fieldnames=headers)
        firstRow = {}
        for i in headers:
            firstRow[i] = i
        dw.writerow(firstRow)
        for row in input:
            dw.writerow(row)


def readRows(inputCSV):
    with open(inputCSV, 'r') as read:
        readCSV = csv.DictReader(read)
        readCSV.fieldnames = [fixHeader(header) for header in readCSV.fieldnames]
        listOfOrderedDics = []
        for row in readCSV:
            listOfOrderedDics.append(row)
        return readCSV.fieldnames, listOfOrderedDics


if __name__ == '__main__':
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    if csvToRead and csvToCreate:
        getCSV = readRows(csvToRead)
        processedCSV(csvToCreate, getCSV[0], getCSV[1])
