import datetime


class Daily_show:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.year_value = record["year"]
            self.occupation = record["googleknowlege_occupation"]
            self.air_date = record["show"]
            self.group_value = record["group"]
            self.guest_value = record["raw_guest_list"]


    def year(self):
        """

        Returns:
            str: The year the show aired

        """
        return int(self.year_value)

    def googleknowlege_occupation(self):
        """

        Returns:
            str: The general profession of the guest

        """
        return str(self.occupation)

    def show(self):
        """

        Returns:
            int: The exact day the show aired

        """
        return str(self.air_date)



    def group(self):
        """

        Returns:
            str: The general group that the guest fits in

        """
        return str(self.group_value)

    def raw_guest_list(self):
        """

        Returns:
            int: The name of the guest

        """
        return str(self.guest_value)



    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return str(self.raw_guest_list())

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Daily_show(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'raw_guest_list'
                                     or key == 'googleknowlege_occupation') + ")"

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
                daily_show = Daily_show(rc)
                ofile.write("# " +  str(idx +1)+ ". " + str(daily_show.raw_guest_list()) + "\n\n")
                ofile.write('* Occupation of Guest: ' + str(daily_show.googleknowlege_occupation()) + '\n') #This needs to be a string to write
                ofile.write('* General Group of Guest: ' + str(daily_show.group()) + '\n')
                ofile.write('* Air Date of Guest Appearance: ' + str(daily_show.show()) + '\n')



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
