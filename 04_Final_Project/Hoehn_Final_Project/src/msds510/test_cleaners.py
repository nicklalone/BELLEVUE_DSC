from msds510.util import transform

if __name__ == '__main__':
    records = [
        dict(show='1/3/99'),
        dict(show='1/3/00'),
        dict(show='1/3/01'),
        dict(show='1/3/02')
    ]
for record in records:
    year = record.get('show')

    print("Days since joined - {0}".format(str(tranform(year))))

