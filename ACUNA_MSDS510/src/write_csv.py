<<<<<<< HEAD
import sys
import csv

# change field names to Python friendly names
def python_friendly_name(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')

#use dictionary reader to input Avengers csf file
#call the function to convert to Python friendly names
#use dictionarly writer to output new field names
def main(input_csv, output_csv):
    with open(input_csv) as f:
        csv_reader = csv.DictReader(f)
        records = [record for record in csv_reader]
        fieldnames = csv_reader.fieldnames

    python_friendly_names = [python_friendly_name(name) for name in fieldnames]
    new_records = [{python_friendly_name(name): value for name, value in record.items()} for record in records]

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

#It will be helpful to write comments in line so that the code is easily understandable and maintainable.

# change field names to Python friendly names
def python_friendly_name(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')

#use dictionary reader to input Avengers csf file
#call the function to convert to Python friendly names
#use dictionarly writer to output new field names
def main(input_csv, output_csv):
    with open(input_csv) as f:
        csv_reader = csv.DictReader(f)
        records = [record for record in csv_reader]
        fieldnames = csv_reader.fieldnames

#Each dictionary is added as alist item in the new list
    python_friendly_names = [python_friendly_name(name) for name in fieldnames]
    new_records = [{python_friendly_name(name): value for name, value in record.items()} for record in records]
	
	#The following is to open the output file in the write mode
	#While using dictionarywriter it is required to add fieldnames in the write mode

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
>>>>>>> 8d9c3c470b3ce5d4b6c1970f922593046371fe98
