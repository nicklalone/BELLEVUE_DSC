import datetime


class Biopic:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.title_value = record["title"]
            self.sites = record["site"]
            self.countrys = record["country"]
            self.year_released = record["year_release"]
            self.box_offices = record["box_office"]
            self.directors = record["director"]
            self.number_of_subjects = record["number_of_subjects"]
            self.type_of_subject = record["type_of_subject"]
            self.race_known = record["race_known"]
            self.subject_race = record["subject_race"]
            self.person_of_color = record["person_of_color"]
            self.subject_sex = record["subject_sex"]
            self.lead_actor_actress = record["lead_actor_actress"]



    def site(self):
        """

        Returns:
            str: The URL of the comic character on the Marvel Wikia

        """
        return self.sites

    def title(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.title_value

    def director(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.directors

    def country(self):
        """

        Returns:
            str: The full name or alias of the character

        """
        return self.countrys



    def year_release(self):
        """

        Returns:
            int: The number of comic books that character
            appeared in as of April 30

        """
        return int(self.year_released)


    def subject_sex(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.subject_sex

    def box_office(self):

        """
            Returns:
            int: The year the character was introduced
            as a full or reserve member of the Avengers

        """
        if(self.box_offices == "-"):
            return ("Not Provided")
        else:
             return self.box_offices


    def lead_actor(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES

        Returns:
            str: Descriptions of deaths and resurrections.

        """
        return self.lead_actor_actress

    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return self.title()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Biopic(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'title'
                                     or key == 'site') + ")"

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
            for idx, rc in enumerate(recordslist, 1):
                biopic = Biopic(rc)
                ofile.write('# {}{} {}'.format(idx, ".", biopic.title()))
                ofile.write('\n\n* {} {}'.format('Year Released: ', str(biopic.year_release())))
                ofile.write('\n* {} {}'.format('Box Office: ', str(biopic.box_office())))
                ofile.write('\n* {} {}'.format('Director: ', biopic.director()))
                ofile.write('\n* {} {}'.format('Country: ', biopic.country()))
                ofile.write('\n* {} {}'.format('Site: ', biopic.site()))
                ofile.write('\n\n## {}'.format("Lead Actors"))
                ofile.write('\n\n{}\n\n'.format(biopic.lead_actor()))

    '''
    This looks like an awesome way to format the comments. I've seen where people have been using the placeholders,
    but never using the {}. Does it work well?
    '''

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
