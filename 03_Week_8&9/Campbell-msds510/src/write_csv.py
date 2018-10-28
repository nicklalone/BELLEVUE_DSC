# What does this function do? I don't understand it and am curious about it.
<<<<<<< HEAD
import sys
import csv


def python_friendly_name(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')


def main(input_csv, output_csv):
    with open(input_csv) as f:
        csv_reader = csv.DictReader(f)
        records = [record for record in csv_reader]
        fieldnames = csv_reader.fieldnames

    # The following line of code is a list comprehension. It creates a list of python_friendly_names

    python_friendly_names = [python_friendly_name(name) for name in fieldnames]

    """The following line is a combination of a list and a dictionary comprehension. 
    It takes the form of (k,v for (k,v) in collection.items)"""
    # I have read conflicting things about using triple quotes for multi-line comments.
    # Quite a few say not to use them because they will be garbage collected at some point.
    new_records = [{python_friendly_name(name): value for name, value in record.items()} for record in records]

    """ Dict Reader Requires us to specify the field names. Especially the writeheader 
        method is what specifies the header values"""

    with open(output_csv, 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=python_friendly_names)
        csv_writer.writeheader()
        csv_writer.writerows(new_records)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: write_csv <input_csv> <output_csv>')
    else:
        main(args[1], args[2])


=======
import sys
import csv


def python_friendly_name(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')

#Method to take in the input file and output file arguments and gather the record and fieldnames from the input file
def main(input_csv, output_csv):
    with open(input_csv) as f:
        csv_reader = csv.DictReader(f)
        records = [record for record in csv_reader]
        fieldnames = csv_reader.fieldnames

    # The following line of code is a list comprehension. It creates a list of python_friendly_names

    python_friendly_names = [python_friendly_name(name) for name in fieldnames]

    """The following line is a combination of a list and a dictionary comprehension. 
    It takes the form of (k,v for (k,v) in collection.items)"""
    # I have read conflicting things about using triple quotes for multi-line comments.
    # Quite a few say not to use them because they will be garbage collected at some point.
    new_records = [{python_friendly_name(name): value for name, value in record.items()} for record in records]

    """ Dict Reader Requires us to specify the field names. Especially the writeheader 
        method is what specifies the header values"""

    with open(output_csv, 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=python_friendly_names)
        csv_writer.writeheader()
        csv_writer.writerows(new_records)

#This code checks if the correct arguments were passed when invoking this script
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: write_csv <input_csv> <output_csv>')
    else:
        main(args[1], args[2])


>>>>>>> 8d9c3c470b3ce5d4b6c1970f922593046371fe98
