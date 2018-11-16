import datetime


class Beer:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.nation = record["country"]
            self.beer_servings = record["beer_servings"]
            self.spirit_servings = record["spirit_servings"]
            self.wine_servings = record["wine_servings"]
            self.total_litres_of_pure_alcohol = record["total_litres_of_pure_alcohol"]


    def country(self):
        """

        Returns:
            str: The name of the country

        """
        return str(self.nation)

    def beer_servings(self):
        """

        Returns:
            str: The number of beers

        """
        return int(self.beer_servings)

    def spirit_servings(self):
        """

        Returns:
            int: The number of mixed drinks

        """
        return int(self.spirit_servings)



    def wine_servings(self):
        """

        Returns:
            str: The glasses of wine

        """
        return int(self.wine_servings)

    def total_litres_of_pure_alcohol(self):
        """

        Returns:
            int: The name of the guest

        """
        return float(self.total_litres_of_pure_alcohol)



    def __str__(self):
        """

        Returns:
            str: A human-readable value for this character

        """
        return str(self.total_litres_of_pure_alcohol())

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Beer(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'total_litres_of_pure_alcohol'
                                     or key == 'beer_servings') + ")"

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
                beer = Beer(rc)
                ofile.write('* Occupation of Guest: '+str(idx +1) + '\n') #This needs to be a string to write
                ofile.write(" " + str(beer.nation()) + " ")

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
