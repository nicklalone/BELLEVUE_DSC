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

    print(new_file[162])  # Dependent on what the assignment means by 162nd row, remember that Python indices start at 0.

if __name__ == '__main__':
    targetFile = argumentexists(1)
    if targetFile:
        csv_read(targetFile)
