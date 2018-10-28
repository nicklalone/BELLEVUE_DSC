import sys, csv
from pprint import pprint

def read_csv(csv_path):
    with open(csv_path) as a:
        csv_reader = csv.reader(a)
        rows = [row for row in csv_reader]

    print('Row 162 printed from csv_reader using csv.reader()')
    pprint(rows[162])

def read_csv_dict(csv_path):
    with open(csv_path) as a:
        csv_reader = csv.DictReader(a)
        fieldnames = csv_reader.fieldnames
        records = [row for row in csv_reader]

    print('Row 161 using dictreader')
    pprint(records[161])
    print('Field Names:')
    pprint(fieldnames)

    #Convert to 'nice names' values from Field Names values
    #stripping out characters and spaces to clean format
    for name in fieldnames:
        nice_name: name.lower().replace(' ','_').replace('/','_').replace('?',"")
        print("'{}', ".format(nice_name))

def main():
    args = sys.argv

    if len(args) < 2:
        print('usage: read_csv <input_csv')
    else:
        read_csv(args[1])


if __name__ == '__main__':
    main()
