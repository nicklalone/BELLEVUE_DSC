import sys
import csv
from msds510.biopic import Biopic
from msds510 import util

#Command: python make_report.py ../data/processed/biopics_processed.csv ../reports/top_ten_biopics.md


def main(infile, outfile):
    """reads an infile, sorts the content, and
       sends the sorted records and an outfile
       destination to printMarkdown to print
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the printMarkdown function with
        sorted records and an outfile to write
        the results to.
    """
    try:
        file = []
        with open(infile, 'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            file = list(reader)

        sorted_records = sorted(file,key=lambda k: float(k['box_office']),reverse=True)[:10]

        biopic = Biopic()
        biopic.to_markdown(sorted_records, outfile)
    except BaseException as e:
        print("Unable to generate comple report.")
        print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


if __name__ == '__main__':
    if util.verify_arguments(sys.argv):
        main(sys.argv[1], sys.argv[2])
