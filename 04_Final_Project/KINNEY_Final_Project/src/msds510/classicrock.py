import datetime


class ClassicRock:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of classicrock data
        """

        if record:
            self.record = record
            self.song_clean = record["song_clean"]
            self.artist_clean = record["artist_clean"]
            self.release_year = record["release_year"]
            self.combined = record["combined"]
            self.first = record["first"]
            self.year = record["year"]
            self.playcount = record["playcount"]
            self.ftimesg = record["f*g"]


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
            classicrocks affiliated team? (True/False)

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
            as a full or reserve member of the classicrocks

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

        return "classicrock(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'name_alias'
                                     or key == 'url') + ")"

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of top 10 classicrock records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            ofile.write(("# Top Ten Classic Rock Songs by Radio Play \n"))
            ofile.write("Data gathered by monitoring 25 classic rock radio stations operating in 30 of the largest" \
                    " metropolitan areas for a week in June 2014. \n")
            for idx, rc in enumerate(recordslist):
                classicrock = ClassicRock(rc)
                ofile.write("## {0} - {1} \n".format(classicrock.song_clean, classicrock.artist_clean))
                ofile.write("* Number of plays: {0}  \n".format(classicrock.playcount))
                ofile.write("* Year Released: {0}  \n".format(classicrock.release_year))
                ofile.write("***\n\n\n")
