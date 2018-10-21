"""
I think we are both guilty of not commenting our code
Here I would put somethig as simple importing csv file
although it may seems obvious it would help someone that will takeover the code or someone new to python programming like myself.
"""

import csv,sys

def argumentexists (index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def csv_read(input):
    new_file =[]
    with open(input) as f:
        file = csv.reader(f, delimiter = ',', quotechar= '"')
        for row in file:
            new_file.append(row)

    print(new_file[162])

if __name__ == '__main__':
    targetFile = argumentexists(1)
    if targetFile:
        csv_read(targetFile)
