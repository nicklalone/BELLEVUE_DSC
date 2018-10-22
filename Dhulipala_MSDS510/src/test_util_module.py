# The line below imports specific methods from the utils file

from msds510.utils import get_date_joined, days_since_joined

# Below is the given input

if __name__ == '__main__':

     records = [
        dict(year='1988', intro='Jun-88'),
        dict(year='1989', intro='May-89'),
        dict(year='2005', intro='5-May'),
        dict(year='2013', intro='13-Nov'),
        dict(year='2014', intro='14-Jan'),
     ]

# The code below iterates through the each and every dictionary in the list
# One dictionary is passed as an arguement at a time
# Empty print statement is used to create a space between the output related to each record
     for record in records:
        year = record.get('year')
        intro = record.get("intro")
        print('Input Record - {}'.format(record))
        print('Date Joined - {}'.format(get_date_joined(year, intro)))
        print('Days Since Joined - {}'.format(days_since_joined(year, intro)))
        print('')


