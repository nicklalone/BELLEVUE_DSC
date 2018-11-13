import datetime
#import sys
#import csv


class Fifa:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of fifa data
        """

        if record:
            self.record = record
            self.country_name = record["country"]
            self.confederation_name = record["confederation"]
            self.population_share_value = record["population_share"]
            self.tv_audience_share_value = record["tv_audience_share"]
            self.gdp_weighted_share_value = record["gdp_weighted_share"]


    def country(self):
        """

        Returns:
            str: The Fifa country

        """
        return self.country_name

    def confederation(self):
        """

        Returns:
            str: The confederation of the fifa country

        """
        return self.confederation_name

    def population_share(self):
        """

        Returns:
            float: the population share

        """
        return float(self.population_share_value)

    def tv_audience_share(self):
        """

        Returns:
            float: tv audience share

        """

        return float(self.tv_audience_share_value)

    def gdp_weighted_share(self):
        """

        Returns:
            gdp_weighted_share

        """
        return float(self.gdp_weighted_share_value)


    def __str__(self):
        """

        Returns:
            str: A human-readable value for this country

        """
        return self.country()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Fifa(" + ",".join(key + "=" + val
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
                fifa = Fifa(rc)
                ofile.write("# " +  str(idx +1)+ ". " + fifa.country() + "\n\n")

                ofile.write("* Confederation: " + fifa.confederation() + "\n")

                ofile.write("* Population Share: " + str(fifa.population_share()) + "\n")

                ofile.write("* TV Audience Share: " + str(fifa.tv_audience_share()) + "\n")

                ofile.write("* GDP Weighted Share: " + str(fifa.gdp_weighted_share()) + "\n\n")

                 #               ofile.write('# {}{} {}'.format(idx, ".", avenger.name_alias()))

                #ofile.write('\n\n* {} {}'.format('Country: ', avenger.country()))

                #ofile.write('\n* {} {}'.format('Confederation: ', avenger.confederation()))

                #ofile.write('\n* {} {}'.format('Population Share: ', avenger.population_share()))

                #ofile.write('\n* {} {}'.format('TV Audience Share: ', avenger.tv_audience_share))

                #ofile.write('\n* {} {}'.format('GDP Weighted Share: ', avenger.gdp_weighted_share))

                #ofile.write('\n\n## {}'.format("Notes"))

                #ofile.write('\n\n{}\n\n'.format(avenger.notes()))
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
