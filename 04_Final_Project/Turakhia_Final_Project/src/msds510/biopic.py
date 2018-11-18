import datetime
import sys

class Biopic:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Biopic data
        """
        if record:
            self.record = record
            self.title = record["title"]
            self.site = record["site"]
            self.country = record["country"]
            self.year_release = record["year_release"]
            self.box_office = record["box_office"]
            self.director = record["director"]
            self.number_of_subjects = record["number_of_subjects"]
            self.subject = record["subject"]
            self.type_of_subject = record["type_of_subject"]
            self.race_known = record["race_known"]
            self.subject_race = record["subject_race"]
            self.person_of_color = record["person_of_color"]
            self.subject_sex = record["subject_sex"]
            self.lead_actor_actress = record["lead_actor_actress"]
			

    def title(self):
        """

        Returns:
            str: The title of the Movie

        """
        return self.title

    def site(self):
        """

        Returns:
            str: The IMDB URL for the Movie

        """
        return self.site

    def country(self):
        """

        Returns:
            str: Movie Country Origin

        """
        return self.country

    def year_release(self):
        """

        Returns:
            int: Year when the movie was released

        """

        return int(self.year_release)

    def box_office(self):
        """

        Returns:
            str: Return Box Office Collections

        """
        if(self.box_office == "-"):
            return ("Box Office Collections Not Available")
        else:
             return self.box_office

    def director(self):
        """

        Returns:
            str: Return Director Name

        """
        return self.director


    def lead_actor_actress(self):
        """

        Returns:
            str: Return Lead Actor\Actress

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
            recordslist: list of Movie records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """

        with open(outfile, 'w', encoding='utf-8') as ofile:
            for idx, rc in enumerate(recordslist):
                biopic = Biopic(rc)
                ofile.write('# ' + str(idx + 1) + '. ' + biopic.title + '\n\n')
                ofile.write('* Box Office Collections: ' + str(biopic.box_office) + '\n')
                ofile.write('* Year Released: ' + str(biopic.year_release) + '\n')
                ofile.write('* Movie Director: ' + str(biopic.director) + '\n')
                ofile.write('* Site: ' + biopic.site + '\n')
                ofile.write('* Lead Actor\Actress: ' + biopic.lead_actor_actress + '\n\n')
# The above will work like this:
#       What is the biopic's name? This should be level 1.
# How may appearances have they had? This will be a bullet point.
# What year did they join? This will be a bullet point.
# How many years since joining? This will be a bullet point.
# What is the biopic's IMBD Site? This will be a bullet point.
# The Lead Actor\Actress section will be last as a level 2 heading.
# followed by the Actor\Actress themselves.


# Remember to refer to the example report in the reports folder
