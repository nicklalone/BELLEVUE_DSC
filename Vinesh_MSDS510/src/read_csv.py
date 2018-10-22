import csv
import sys

def main():
    with open(sys.argv[1], newline='') as f:
        csv_reader = csv.reader(f, delimiter=',')
        rows = [row for row in csv_reader]
        print(rows[162])


if __name__ == '__main__':
    main()
