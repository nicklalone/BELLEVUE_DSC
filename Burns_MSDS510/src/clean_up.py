## read data from file
## This doesn't work in PyCharm
lines = open('avengers.csv').readlines()
type(lines)



## Convert lines to rows
rows = []
for line in lines:
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
    fieldnames.append(hv_clean)
print(fieldnames)



## Create dict-based record
records =[]
ct1 = 1
for x in rows:
    d = dict(zip(fieldnames, rows[ct1]))
    records.append(d)
    if ct1 == 172:
        break
    ct1 = ct1+1
print(records[50])
type(records[32])



## Convert record values to appropriate type
## I need to simplify with *args and **kwargs...I think???
ct2 = 0
for y in records:
    records[ct2]["appearances"]=int(records[ct2]["appearances"])
    records[ct2]["year"]=int(records[ct2]["year"])
    records[ct2]["years_since_joining"]=2018-records[ct2]["year"]

    if records[ct2]['current'] == 'NO': records[ct2]['current'] = 'False'
    elif records[ct2]['current'] == 'YES': records[ct2]['current'] = 'True'
    if records[ct2]['death1'] == 'YES': records[ct2]['death1'] = 'True'
    elif records[ct2]['death1'] == 'NO': records[ct2]['death1'] = 'False'
    if records[ct2]['death2'] == 'YES': records[ct2]['death2'] = 'True'
    elif records[ct2]['death2'] == 'NO': records[ct2]['death2'] = 'False'
    if records[ct2]['death3'] == 'YES': records[ct2]['death3'] = 'True'
    elif records[ct2]['death3'] == 'NO': records[ct2]['death3'] = 'False'
    if records[ct2]['death4'] == 'YES': records[ct2]['death4'] = 'True'
    elif records[ct2]['death4'] == 'NO': records[ct2]['death4'] = 'False'
    if records[ct2]['death5'] == 'YES': records[ct2]['death5'] = 'True'
    elif records[ct2]['death5'] == 'NO': records[ct2]['death5'] = 'False'
    if records[ct2]['return1'] == 'YES': records[ct2]['return1'] = 'True'
    elif records[ct2]['return1'] == 'NO': records[ct2]['return1'] = 'False'
    if records[ct2]['return2'] == 'YES': records[ct2]['return2'] = 'True'
    elif records[ct2]['return2'] == 'NO': records[ct2]['return2'] = 'False'
    if records[ct2]['return3'] == 'YES': records[ct2]['return3'] = 'True'
    elif records[ct2]['return3'] == 'NO': records[ct2]['return3'] = 'False'
    if records[ct2]['return4'] == 'YES': records[ct2]['return4'] = 'True'
    elif records[ct2]['return4'] == 'NO': records[ct2]['return4'] = 'False'
    if records[ct2]['return5'] == 'YES': records[ct2]['return5'] = 'True'
    elif records[ct2]['return5'] == 'NO': records[ct2]['return5'] = 'False'
    records[ct2]['notes'] = records[ct2]['notes'].strip(' \n')
    records[ct2]
    if ct2 == 171:
        break
    ct2 = ct2 + 1

print(len(records)," ",type(records[42]))
