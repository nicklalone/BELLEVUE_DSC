import sys, csv

with open('avengers.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',') 
    for row in csv_reader:
        print(', '.join(row))
        
            