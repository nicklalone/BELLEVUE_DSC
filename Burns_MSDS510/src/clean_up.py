## read data from file
lines = open('avengers.csv').readlines()
type(lines)



## Convert lines to rows
rows = [] for line in lines:
    line_split = line.split(',')
    if len(line_split)==21:
        rows.append(line_split)
    Row_Count = len(rows)
    print("Number of Rows:", Row_Count)



## Create header
header = rows[0]
fieldnames = []
for hv in header:
    hv_lower = hv.lower()
    hv_clean = hv_lower.replace('/','_').strip('?').strip('\n').replace(' ','_')
    fieldnames.append(hv_clean) print(fieldnames)



## Create dict-based record
records =[]
countera = 1
for x in rows:
    d = dict(zip(fieldnames, rows[countera]))
    records.append(d)
    if countera == 172:
        break countera = countera+1
print(records[50])
type(records[32])



## Convert record values to appropriate type
## I need to simplify with *args and **kwargs...I think???
counterb = 0
for y in records:
    records[counterb]["appearances"]=int(records[counterb]["appearances"])
    records[counterb]["year"]=int(records[counterb]["year"])
    records[counterb]["years_since_joining"]=2018-records[counterb]["year"]

    if records[counterb]['current'] == 'NO': records[counterb]['current'] = 'False'
    elif records[counterb]['current'] == 'YES': records[counterb]['current'] = 'True'
    if records[counterb]['death1'] == 'YES': records[counterb]['death1'] = 'True'
    elif records[counterb]['death1'] == 'NO': records[counterb]['death1'] = 'False'
    if records[counterb]['death2'] == 'YES': records[counterb]['death2'] = 'True'
    elif records[counterb]['death2'] == 'NO': records[counterb]['death2'] = 'False'
    if records[counterb]['death3'] == 'YES': records[counterb]['death3'] = 'True'
    elif records[counterb]['death3'] == 'NO': records[counterb]['death3'] = 'False'
    if records[counterb]['death4'] == 'YES': records[counterb]['death4'] = 'True'
    elif records[counterb]['death4'] == 'NO': records[counterb]['death4'] = 'False'
    if records[counterb]['death5'] == 'YES': records[counterb]['death5'] = 'True'
    elif records[counterb]['death5'] == 'NO': records[counterb]['death5'] = 'False'
    if records[counterb]['return1'] == 'YES': records[counterb]['return1'] = 'True'
    elif records[counterb]['return1'] == 'NO': records[counterb]['return1'] = 'False'
    if records[counterb]['return2'] == 'YES': records[counterb]['return2'] = 'True'
    elif records[counterb]['return2'] == 'NO': records[counterb]['return2'] = 'False'
    if records[counterb]['return3'] == 'YES': records[counterb]['return3'] = 'True'
    elif records[counterb]['return3'] == 'NO': records[counterb]['return3'] = 'False'
    if records[counterb]['return4'] == 'YES': records[counterb]['return4'] = 'True'
    elif records[counterb]['return4'] == 'NO': records[counterb]['return4'] = 'False'
    if records[counterb]['return5'] == 'YES': records[counterb]['return5'] = 'True'
    elif records[counterb]['return5'] == 'NO': records[counterb]['return5'] = 'False'
records[counterb]['notes'] = records[counterb]['notes'].strip(' \n')
records[counterb]
if counterb == 171:
    break counterb = counterb + 1

print(len(records)," ",type(records[42]))
