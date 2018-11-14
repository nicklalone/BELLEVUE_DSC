import datetime

class Broadcast:
    def __init__(self, record = None):
        '''
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
        record (dict): Dictionary-based record of Broadcast data
        '''
        if record:
            self.record = record
            self.year = record['year']
            self.googleknowledge_occupation= record['googleknowledge_occupation']
            self.show = record['show']
            self.group = record['group']
            self.raw_guest_list = record['raw_guest_list']


    def year(self):
        '''

        :return:
        '''
        return int(year.self)

    def googleknowledge_occupation(self):
        '''

        :return: str Occupation as listed in Google Knowledge
        '''
        return self.googleknowledge_occupation

    def show(self):
        '''

        :return: datetime.date Air date of show as a datetime object
        '''
        return datetransform(self.show)

    def group(self):
        '''

        :return: str Group category of guests
        '''
        return self.group

    def raw_guest_list(self):
        '''

        :return: str Listing of guest list for show
        '''
        return self.raw_guest_list

    def years_since_aired(self):
        '''

        :return: int years since air date
        '''
        return datetime.date.today().year - self.year()

    def datetransform (date):
        """
        :param date: date in string format mm/dd/yy
        :return: datetime object
        """
        temp_date = date.replace('/', ' ')
        date_list = temp_date.split(' ')
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
        if year > 98:
            year = year + 1900
        else:
            year = year + 2000
        new_date = datetime.date(year, month, day)
        return new_date

    def to_markdown(self, showlist, outfile):
        '''

        :param showlist: Dict records of shows
        :param outfile: string of output file location
        :return: prints contents of showlist in a formatted report
        '''
        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(showlist):
                ofile.write('# ' + str(idx +1) + '. ' + rc['show'] + '\n' + '\n')
                ofile.write('* Guest list: ' + (rc['raw_guest_list']) + '\n')
                ofile.write('* Group: ' + (rc['group']) + '\n')
                ofile.write('* Year Aired: ' + str(rc['year']) +'\n')
                ofile.write('* Years Since Aired: ' + str(rc['years_since_aired']) +'\n' +'\n')
