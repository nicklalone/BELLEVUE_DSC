import datetime


class Avenger:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.url_value = record["url"]
            self.alias = record["name_alias"]
            self.appearances_count = record["appearances"]
            self.current = record["current"]
            self.death1 = record["death1"]
            self.death2 = record["death2"]
            self.death3 = record["death3"]
            self.death4 = record["death4"]
            self.death5 = record["death5"]
            self.first_appearance = record["full_reserve_avengers_intro"]
            self.gender_value = record["gender"]
            self.honorary = record["honorary"]
            self.notes_value = record["notes"]
            self.probationary_introl = record["probationary_introl"]
            self.return1 = record["return1"]
            self.return2 = record["return2"]
            self.return3 = record["return3"]
            self.return4 = record["return4"]
            self.return5 = record["return5"]
            self.year_value = record["year"]
            self.years_since_joining_value = record["years_since_joining"]

    def url(self):
        """

        Returns:
            str: The URL of the comic character on the Marvel Wikia

        """
        return self.url_value

    def name_alias(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.alias

    def appearances(self):
        """

        Returns:
            int: The number of comic books that character
            appeared in as of April 30

        """
        return int(self.appearances_count)

    def is_current(self):
        """

        Returns:
            bool: Is the member currently active on an
            avengers affiliated team? (True/False)

        """

        if not self.current.strip():
            return None
        else:
            return True if self.current == 'YES' else False

    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.gender_value

    def year(self):
        """

        Returns:
            int: The year the character was introduced
            as a full or reserve member of the Avengers

        """
        return int(self.year_value)

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

        return (datetime.date(self.year(), self.get_month(), 1))

    def days_since_joining(self):
        """

        Returns:
            int: The number of integer days since the character joined

        """
        rval = datetime.date.today() - self.date_joined()
        rval = rval.days
        return rval

    def years_since_joining(self):
        """

        Returns:
            int: The number of integer years since the character joined

        """

        return datetime.date.today().year - self.year()

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES

        Returns:
            str: Descriptions of deaths and resurrections.

        """
        return self.notes_value.strip()

    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return self.name_alias()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Avenger(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'name_alias'
                                     or key == 'url') + ")"

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of top 10 avenger records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                avenger = Avenger(rc)
                ofile.write('# ' + str(idx + 1) + '. ' + avenger.name_alias() + '\n\n')
                ofile.write('* Number of Appearances: ' + str(avenger.appearances()) + '\n') #This needs to be a string to write
                ofile.write('* Year Joined: ' + str(avenger.year()) + '\n')
                ofile.write('* Years Since Joining: ' + str(avenger.years_since_joining()) + '\n')

                ofile.write('* URL: ' + avenger.url() + '\n\n')
                ofile.write('## Notes\n\n')
                ofile.write(avenger.notes() + '\n\n')

                # each line needs to be formatted to return what's needed for the Markdown file. There are many different ways
                # to do this. The below comments have good pointers. I would focus on using the polymorphism aspect of the + operator,
                # converting things to strings, and using '\n' to create new lines.
                """
                We can use \n for creating new line while writing into the file.
                We can use operator overlading concept and use + sign to add to strings before writing into the file.
                We can use str function to convert int's to string before writing into the file.
                We can use # for level 1 header label and double # for level 2 header labels.
                We can use * for bullet list.
                """

                #As a further tip to the above, remember that the index (idx) starts at zero
                #so we'll want to add 1 to it before converting to a string

# The above will work like this:
#       What is the avenger's name? This should be level 1.
# How may appearances have they had? This will be a bullet point.
# What year did they join? This will be a bullet point.
# How many years since joining? This will be a bullet point.
# What is the avenger's URL? This will be a bullet point.
# The notes section will be last as a level 2 heading.
# followed by the notes themselves.
# Spacing will be up to you.

# Remember to refer to the example report in the reports folder
