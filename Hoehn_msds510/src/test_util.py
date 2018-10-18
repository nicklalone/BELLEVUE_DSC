from msds510.util import get_date_joined, days_since_joined, get_month

if __name__ == '__main__':
    records = [
        dict(year='1988', intro = 'Jun-88'),
        dict(year='1989', intro = 'May-89'),
        dict(year='2005', intro = '5-May'),
        dict(year='2013', intro = '12-Nov'),
        dict(year='2014', intro = '14-Jan')
    ]
for record in records:
    year = record.get('year')
    intro = record.get('intro')
    print("Input record - {year : " + year + ", intro : " + intro +"}")
    print("Date joined - {0}".format(str(get_date_joined(year, intro))))
    print("Days since joined - {0}".format(str(days_since_joined(year, intro))))

