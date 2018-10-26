#Open Avengers file as dictionary records from csv file

import sys, csv

with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[])
        
            