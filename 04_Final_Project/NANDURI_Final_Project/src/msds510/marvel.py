import datetime

"""
Marvel class to process the dictionary records.
Used in make_report.py.
"""


class Marvel:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.
        Args:
            record (dict): Dictionary-based record of Marvel data
        """

        if record:
            self.record = record
            self.page_id = record["page_id"]
            self.name = record["name"]
            self.urlslug = record["urlslug"]
            self.id = record["id"]
            self.align = record["align"]
            self.eye = record["eye"]
            self.hair = record["hair"]
            self.sex = record["sex"]
            self.gsm = record["gsm"]
            self.alive = record["alive"]
            self.appearances = record["appearances"]
            self.first_appearance = record["first_appearance"]
            self.year = record["year"]
            self.days_since_first_appearance = record["days_since_first_appearance"]

    def fn_urlslug(self):
        """
        Returns:
            str: The URL of the comic character on the Marvel Wikia
        """
        return self.urlslug

    def fn_name(self):
        """
        Returns:
            str: The name of the character
        """
        return self.name

    def fn_appearances(self):
        """
        Returns:
            int: The number of comic books that character
            appeared in as of April 30
        """
        return int(self.appearances)

    def fn_year(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Marvels
        """
        return int(self.year)

    def get_month(self):
        months = ["jan", "feb", "mar", "apr", "may", "jun",
                  "jul", "aug", "sep", "oct", "nov", "dec"]

        for i in range(0, len(months)):
            if months[i] in self.first_appearance.lower():
                return i + 1
        return 0

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined
        """
        return datetime.date(self.year(), self.get_month(), 1)

    def fn_days_since_joining(self):
        """
        Returns:
            int: The number of integer days since the character joined
        """
        rval = datetime.date.today() - self.date_joined()
        rval = rval.days
        return rval

    def fn_years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        return datetime.date.today().year - self.fn_year()

    def __repr__(self):
        """
        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return "Marvel(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'name'
                                     or key == 'urlslug') + ")"

    def to_markdown(self, recordslist, outfile):
        """
        Function that takes a list of records, formats them and prints them to an output file.
        Args:
            recordslist: list of top 10 marvel records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            ofile.write('\n## Raghu Raman Nanduri - Final Project 510  \n\n')
            ofile.write('***This report shows the top 10 appearances of the Marvel comic charecters*** \n')
            ofile.write('Source link for this project is :'
                        '  *https://github.com/fivethirtyeight/data/tree/master/comic-characters* \n\n')

            for idx, rc in enumerate(recordslist):
                marvel = Marvel(rc)
                # Writing report file for - Top ten appearances
                ofile.write(' **%d. %s ** \n\n' % (idx+1, marvel.fn_name()))
                ofile.write('   - Number of Appearances: %d \n' % (marvel.fn_appearances()))
                ofile.write('   - Year Joined: %d \n' % (marvel.fn_year()))
                ofile.write('   - Years Since Joining: %d \n' % (marvel.fn_years_since_joining()))
                ofile.write('   - URL: %s \n\n' % (marvel.fn_urlslug()))


