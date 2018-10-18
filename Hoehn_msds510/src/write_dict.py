import csv,sys

def argumentexists (index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def make_nice_name (name):
    return name.replace('?','').replace(' ','_').replace('-','_').strip('\n').lower()

def dict_write(input, output):
    with open(input) as f:
        reader = csv.DictReader(open(input))
        header = reader.fieldnames
        records = [row for row in reader]
    nice_names = [make_nice_name(field) for field in header]
    new_records = [{make_nice_name(name): value for name, value in record.items()} for record in records]

    with open(output, 'w')as g:
        writer = csv.DictWriter(g, fieldnames=nice_names)
        writer.writeheader()
        writer.writerows(new_records)

if __name__ == '__main__':
    args = sys.argv
    if len(args) <3:
        print('usage: dict_write <input> <output>')
    else:
        dict_write(args[1], args[2])
