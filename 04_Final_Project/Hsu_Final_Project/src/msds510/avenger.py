# Avenger class to assist with creating a markdown report.


class Avenger:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of unisex data
        """

        if record:
            self.record = record
            self.name_value = record['name']
            self.total_value = round(float(record['total']))
            self.male_share_value = round(float(record['male_share']) * 100, 2)
            self.female_share_value = round(float(record['female_share']) * 100, 2)
            self.gap_value = round(float(record['gap']) * 100, 2)

    # Method Definitions

    def name(self):
        # Returns the unisex name that are commonly used.
        return self.name_value

    def total(self):
        # Returns the total number of Americans with the name
        return self.total_value

    def male_share(self):
        # Returns the percentage of people with the name that are male
        return self.male_share_value

    def female_share(self):
        # Returns the percentage of people with the name that are female
        return self.female_share_value

    def gap(self):
        # Returns the percentage gap between males and females (absolute value)
        return self.gap_value

    # def __str__(self):
    #     # Reads the object as a string
    #     return self.name()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """

        return "Avenger(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'name_alias'
                                     or key == 'url') + ")"

    def to_markdown(self, records_list, outfile):
        # Takes a list of records and writes out a formatted output file.
        # Arguments:
            # records_list: list of records utilized in the Avengers class
        with open(outfile, 'w') as ofile:
            ofile.write('# List of the top 10 names with the lowest gender gap percentage.\n\n')
            for idx, rc in enumerate(records_list, 1):
                avenger = Avenger(rc)
                ofile.write('## ' + str(idx) + '. ' + avenger.name() + '\n\n')
                ofile.write('* Total number of people with the name: ' + str(avenger.total()) + '\n')
                ofile.write('* Percent of males: ' + str(avenger.male_share()) + '%\n')
                ofile.write('* Percent of females: ' + str(avenger.female_share()) + '%\n')
                ofile.write('* Gap: ' + str(avenger.gap()) + '%\n\n')
