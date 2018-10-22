from modules.dateUtility import get_date_joined, days_since_joined
records - [
    dict(year='1998', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-jan'),
]

for record in records:
    print("Input Record -", record)
    joinDate = get_date_joined((record['year']), (record['intro']))
    print("Date Joined -", joinDate)
    daysSince = days_since_joined((record['year']), (record['intro']))
    print("Days since Joined -", daysSince,'\n ')

    #great use of the dictionary. Something that helps me keep track of the changes is commenting what is being changed and why. Could save some time in the future.
