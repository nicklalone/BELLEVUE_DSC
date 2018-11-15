import datetime


class Avenger:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of DC data
        """

        if record:
            self.record = record
            self.id_value = record["ID"]
            self.align = record["ALIGN"]
            self.eye_color = record["EYE"]
            self.hair_color = record["HAIR"]
            self.sex = record["SEX"]
            self.gsm = record["GSM"]
            self.living_status = record["ALIVE"]
            self.appearance_count = record["APPEARANCES"]
            self.first_appearance = record["FIRST APPEARANCE"]
            self.appearance_year = record["YEAR"]
            self.years_since_joining_value = record["years_since_joining"]

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
        return self.eye_color

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
        return self.hair_color

    def gsm(self):
        """
        Returns:
             str: GSM Status of DC Character
        """
        return self.gsm

    def alive(self):
        """
        Returns:
            str: Living status of DC Character
        """
        return self.alive

    def appearances(self):
        """

        Returns:
            int: The number of appearances of comic book DC Character

        """
        return int(self.appearance_count)

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
                ofile.write('# ' + str(idx) + str(avenger.name_alias()) + '\n\n')
                ofile.write('* Number of Appearances : ' + str(avenger.appearances()) +'\n')
                ofile.write('* Year Joines: ' + str(avenger.year()) + '\n')
                ofile.write('* Years Since Joining: '+ str(avenger.years_since_joining()) + '\n')
                ofile.write('* URL: ' + str(avenger.url()) + '\n')
                ofile.write('## Notes' + '\n')
                ofile.write(avenger.notes() + '\n')
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
