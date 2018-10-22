<<<<<<< HEAD
# read data from file
# This doesn't work in PyCharm
=======
## read data from file
## This doesn't work in PyCharm
## This won't work in PyCharm as it's not a function and I don't think you can call it to run it using any input file. If you needed to use this script on any other file, you would need to rewrite
## this file for the new file.
## I like how you use interations, but it would only work when you know how long a file
## is before you run the file. To make the interation more general, in your third block of coding, you could use
# if ctl == len(file)-1
#     break
>>>>>>> eefa1e681afad7ee45e9467b2d9da4002536b14a
lines = open('avengers.csv').readlines()
type(lines)


# Convert lines to rows
rows = []
for line in lines:
    line_split = line.split(',')
    if len(line_split) == 21:  # whitespace around operators
        rows.append(line_split)
    Row_Count = len(rows)
    print("Number of Rows:", Row_Count)
'''
This code will ignore lines that have ','s in the middle.
I used the following code to get around that problem

def csv_read(input):
    new_file =[]
    with open(input) as f:
        file = csv.reader(f, delimiter = ',', quotechar= '"')
        for row in file:
            new_file.append(row)

This will read the file and append a the new row.  Using the quote characters
means that anything between the double apostrophes will be read as part of the
file. This avoids the problem of splitting too much with commas as a delimiter.            
'''

# Create header
header = rows[0]
fieldnames = []
for hv in header:
    hv_lower = hv.lower()
    hv_clean = hv_lower.replace('/', '_').strip('?').strip('\n').replace(' ', '_')  # space after commas
    fieldnames.append(hv_clean)
print(fieldnames)


# only use one hash tag for comments, only 2 blank lines between
# Create dict-based record
records = []
ct1 = 1
for x in rows:
    d = dict(zip(fieldnames, rows[ct1]))
    records.append(d)
    if ct1 == 172:
        break
    ct1 = ct1+1
print(records[50])
type(records[32])


# Convert record values to appropriate type
# I need to simplify with *args and **kwargs...I think???
ct2 = 0
for y in records:
    int(records[ct2]["appearances"])
    int(records[ct2]["year"])
    records[ct2]["years_since_joining"] = 2018-records[ct2]["year"]  # whitespace around operator
# new line after colon
    if records[ct2]['current'] == 'NO':
        records[ct2]['current'] = 'False'
    elif records[ct2]['current'] == 'YES':
        records[ct2]['current'] = 'True'
    if records[ct2]['death1'] == 'YES':
        records[ct2]['death1'] = 'True'
    elif records[ct2]['death1'] == 'NO':
        records[ct2]['death1'] = 'False'
    if records[ct2]['death2'] == 'YES':
        records[ct2]['death2'] = 'True'
    elif records[ct2]['death2'] == 'NO':
        records[ct2]['death2'] = 'False'
    if records[ct2]['death3'] == 'YES':
        records[ct2]['death3'] = 'True'
    elif records[ct2]['death3'] == 'NO':
        records[ct2]['death3'] = 'False'
    if records[ct2]['death4'] == 'YES':
        records[ct2]['death4'] = 'True'
    elif records[ct2]['death4'] == 'NO':
        records[ct2]['death4'] = 'False'
    if records[ct2]['death5'] == 'YES':
        records[ct2]['death5'] = 'True'
    elif records[ct2]['death5'] == 'NO':
        records[ct2]['death5'] = 'False'
    if records[ct2]['return1'] == 'YES':
        records[ct2]['return1'] = 'True'
    elif records[ct2]['return1'] == 'NO':
        records[ct2]['return1'] = 'False'
    if records[ct2]['return2'] == 'YES':
        records[ct2]['return2'] = 'True'
    elif records[ct2]['return2'] == 'NO':
        records[ct2]['return2'] = 'False'
    if records[ct2]['return3'] == 'YES':
        records[ct2]['return3'] = 'True'
    elif records[ct2]['return3'] == 'NO':
        records[ct2]['return3'] = 'False'
    if records[ct2]['return4'] == 'YES':
        records[ct2]['return4'] = 'True'
    elif records[ct2]['return4'] == 'NO':
        records[ct2]['return4'] = 'False'
    if records[ct2]['return5'] == 'YES':
        records[ct2]['return5'] = 'True'
    elif records[ct2]['return5'] == 'NO':
        records[ct2]['return5'] = 'False'
    records[ct2]['notes'] = records[ct2]['notes'].strip(' \n')
    if ct2 == 171:  # deleted line that does nothing
        break
    ct2 = ct2 + 1

<<<<<<< HEAD
print(len(records), " ", type(records[42]))
=======
print(len(records)," ",type(records[42]))

#Great work! Something that helps me is printing what is currently happening in the code. For example, print("Counting number of years"). etc. - Myrna
>>>>>>> eefa1e681afad7ee45e9467b2d9da4002536b14a
