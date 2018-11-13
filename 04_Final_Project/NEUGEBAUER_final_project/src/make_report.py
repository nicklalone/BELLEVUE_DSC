import sys
import csv
import yaml
from bad_drivers.bad_driver import BadDrivers

def main():
    """
    Gets the processed CSV and MD file names from the .yml file then
    calls the function to generate the MD file.
    """
    try:
        config = yaml.safe_load(open('../config/config.yml'))
        processed_csv = config.get('OutputFile')
        output_md = config.get('ReportFile')
        generate_report(processed_csv, output_md)
        print('Completed creating the MD file.')
    except:
        print('An exception occured in the main method.', sys.exc_info())

def generate_report(infile, outfile):
    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file, key=lambda k: float(k['number_of_drivers_involved_in_fatal_collisions_per_billion_miles']), reverse=True)[:10]

    bad_drivers = BadDrivers()
    bad_drivers.to_markdown(sortedRecords, outfile)

if __name__ == '__main__':
    main()
