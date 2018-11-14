class fifa_countries_audiences:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.country = record["country"]
            self.confederation = record["confederation"]
            self.population_share = record["population_share"]
            self.tv_audience_share_value = record["tv_audience_share"]
            self.gdp_weighted_share_value = record["gdp_weighted_share"]


    def country(self):

        return str(self.country)

    def confederation(self):

        return str(self.confederation)

    def population_share(self):

        return int(self.population_share)



    def tv_audience_share(self):

        return int(self.tv_audience_share)

    def tv_audience_share(self):

        return int(self.tv_audience_share)



    def __int__(self):

        return int(self.gdp_weighted_share())

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "fifa_countries_audience(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'country'
                                     or key == 'confederation') + ")"

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
                fifa_countries_audiences = Fifa_countries_audiences(rc)
                ofile.write("# " +  str(idx +1)+ ". " + str(fifa_countries_audiences.countries()) + "\n\n")
                ofile.write('* Conferation: ' + str(fifa_countries_audiences.conferation()) + '\n') #This needs to be a string to write
                ofile.write('* Population: ' + str(fifa_countries_audiences.population_share()) + '\n')
                ofile.write('* Audience Share: ' + str(fifa_countries_audiences.tv_audience_share()) + '\n')



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
