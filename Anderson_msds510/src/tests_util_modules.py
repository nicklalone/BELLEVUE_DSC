from msds510.util import get_date_joined, days_since_joined

records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan'),
]

for record in records:
    print("Input Record -", record)
    joinDate = get_date_joined((record['year']), (record['intro']))
    print("DateJoined =", joinDate)
    daysSince = days_since_joined((record['year']), (record['intro']))
    print("days since Joined -", daysSince, '\n')
