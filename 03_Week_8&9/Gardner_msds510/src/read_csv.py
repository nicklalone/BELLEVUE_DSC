## I do not comment on my code at work, because it is so simple.
## Now I can see why it is important to provide context.
## Would the following comments work?


## Bring CSV in PyCharm
import sys
import csv

## Determine if there is a line that need to be imported
def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

## Create and fill "rows" table
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
