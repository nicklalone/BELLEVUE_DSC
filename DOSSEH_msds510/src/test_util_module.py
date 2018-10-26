from msds.util import get_date_joined, days_since_joined

if __name__ == '__main__':
    records = [
        dict(year='1988', intro='Jun-88'),
        dict(year='1989', intro='May-89'),
        dict(year='2005', intro='5-May'),
        dict(year='2013', intro='13-Nov'),
        dict(year='2014', intro='14-Jan'),
    ]

    for record in records:
        year = record.get('year')
        intro = record.get('intro')
        print('Input Record - {}'.format(record))
        print('Date joined - {}'.format(get_date_joined(year,intro)))
        print('Days since joined - {}'.format(days_since_joined(year, intro)))
        print('')
