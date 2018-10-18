import csv,sys

def argumentexists (index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


def dict_read(input):
    reader = csv.DictReader(open(input))
    for line in reader:

if __name__ == '__main__':
    targetFile = argumentexists(1)
    if targetFile:
        dict_read(targetFile)
