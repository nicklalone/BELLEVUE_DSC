from msds510.utils.date_functions import get_date_joined, days_since_joined

records = [dict(year='1988', intro='Jun-88'),
           dict(year='1989', intro='May-89'),
           dict(year='2005', intro='5-May'),
           dict(year='2013', intro='13-Nov'),
           dict(year='2014', intro='14-Jan')
           ]

for x in records:
    date_joined = get_date_joined(x['year'], x['intro'])
    days_joined = days_since_joined(x['year'], x['intro'])
    print('Input Record -', x)
    print('Date joined -', date_joined)
    print('Days since joined -', days_joined, '\n')
