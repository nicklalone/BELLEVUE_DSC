from msds510.util import get_date_joined, days_since_joined


#It is clear which records your are working with, but without access to the assignment as a reviewer,
#I might be a little unclear why these particular records were selected
#Would maybe suggest a quick comment section/descriptor of the module at the top of its intended use
#-OR- if it is meant to be scalable, modifying with more flexible inputs based on conditional 
#statements (i.e. don't rely on implicitly identifying the years and introductions,
# rather using the readlines module and reading the values into the 
#'year' and 'intro' storage lists)

if __name__ == '__main__':
    records = [
        dict(year='1988', intro='Jun-88'),
        dict(year='1989', intro='May-89'),
        dict(year='2005', intro='5-May'),
        dict(year='2013', intro='13-Nov'),
        dict(year='2014', intro='14-Jan'),
    ]

#prints the year an Avengers character joined
#calculated and prints the number of days since the character joined the Avengers
    for record in records:
        year = record.get('year')
        intro = record.get('intro')
        print('Input Record - {}'.format(record))
        print('Date joined - {}'.format(get_date_joined(year, intro)))
        print('Days since joined - {}'.format(days_since_joined(year, intro)))
        print('')
