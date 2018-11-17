import datetime


class dc_characters:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of DC data
        """

        if record:
            self.record = record
            self.id_value = record["page_id"]
            self.name = record["name"]
            self.urlslug = record["urlslug"]
            self.id = record["id"]
            self.align = record["align"]
            self.eye_color = record["eye"]
            self.hair_color = record["hair"]
            self.sex = record["sex"]
            self.appearance_count = record["appearances"]
            self.year = record["year"]
            # self.years_since_joining_value = record["years_since_joining"]

    def id(self):
        """

        Returns:
            str: The ID Number from the DC list

        """
        return int(self.id_value)

    def alignment(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.align

    def eye_color(self):
        """
        Returns:
            str: Eye Color of DC Character
        """
        return self.eye

    def hair_color(self):
        """
        Returns:
            str: Hair COlor of DC Character
        """
        return self.hair_color

    def sex(self):
        """
        Returns:
             str: Sex of DC Character
        """
        return self.sex

    def alive(self):
        """
        Returns:
            str: Living status of DC Character
        """
        return self.alive

    def appearance_count(self):
        """

        Returns:
            int: The number of appearances of comic book DC Character

        """
        return int(self.appearances)

    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.gender

    def urlslug(self):
        """

        Returns:
            str: The urlslug of the character

        """
        return self.urlslug

    def year(self):
        """

        Returns:
            int: The year the character was introduced
            as a full or reserve member of the Avengers

        """
        return int(self.year)

    def get_month(self):
        months = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november", "december"]

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
            recordslist: list of top 10 dc records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                character = dc_characters(rc)
                ofile.write('# ' + str(idx) + str(dc-characters.name()) + '\n\n')
                ofile.write('* Number of Appearances : ' + str(dc-characters.appearances()) +'\n')
                ofile.write('* Year Joined: ' + str(dc-characters.year()) + '\n')
                ofile.write('* Years Since Joining: '+ str(dc-characters.years_since_joining()) + '\n')
                ofile.write('* URL: ' + str(dc-characters.urlslug()) + '\n')

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
