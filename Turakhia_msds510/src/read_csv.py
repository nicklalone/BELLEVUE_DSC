import sys
import csv

# Based on the indents, this Python script doesn't accomplish the task set in the assignment. It only defines the function "argumentexists."
# Everything is completed when "argumentexists" is run. But I don't think you can run this separately since there is no sys.argv input for it.
def argumentexists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

    rows =[]  # This will clear out the 'rows' list every time "argumentexists" is ran.
    # The "readRows" function is local to "argumentexists" and can't be used outside of this scope (i.e. you can't use it outside of the "argumentexists" function.
    def readRows(inputCSV):
        readCSV = csv.reader(read)  # 'read' should be 'inputCSV'. 'read' is not a defined variable. Also 'inputCSV' is never used.
        for row in readCSV:
            rows.append(row)
            # These 2 print statements will run for every iteration. They should be outside of the 'for' loop.
            print(rows[161])  # This will result in an error since there is no 161st index on the first iteration.
            print("ADFOSFOSFODSFOSFOSDF")

            # This is inside the 'for' loop so every iteration will run the 2 functions.
            if __name__ =="__main__":
                csvToRead = argumentExists(1)  # Keep an eye on cases. Python is very case-sensitive. This is an undefined function but "argumentexists" is.
                readRows (csvToRead)
