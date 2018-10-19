import sys
 
def argumentExists(index): #function to try get arguments that will not crash program if argument out of bounds
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]
 

    avengers = open(avengers.csv,'rb')
    avengersdecoded = avengers.read()
    avengersdecoded = avengersdecoded.decode('ISO-8859-1')
    avengers.close()
    writeAvengers = open(avengers_utf8.csv, 'w')
    writeAvengers.write(avengersdecoded)
    writeAvengers.close()
