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
            self.country_value = record['country']
            self.beer_served_value = record['beer_served']
            self.spirit_served_value = record['spirit_served']
            self.wine_served_value = record['wine_served']
            self.total_litres_of_pure_alcohol_value = record['total_litres_of_pure_alcohol']

    # Method Definitions

    def country(self):
        # Returns the country
        return self.country_value

    def beer_served(self):
        # Returns the liters of beer served
        return self.beer_served_value

    def spirit_served(self):
        # Returns the liters of spirit served
        return self.spirit_served_value

    def wine_served(self):
        # Returns the liters of wine served
        return self.wine_served_value

    def total_litres_of_pure_alcohol(self):
        # Returns the total of liters of pur alcohol consumed
        return self.total_litres_of_pure_alcohol_value


    #Joe F.: May have to remove the '()' after country
    def __str__(self):
        # Reads the object as a string
        return self.country()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """
        
        return "Avenger(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     # Joe F.: You'll probably want to replace this with the key value for
                                     # whatever you're wanting to title your report; 'name_alias' 
                                     # comes from the original data set for Avengers
                                     if key == 'name_alias'
                                     or key == 'url') + ")"

    def to_markdown(self, records_list, outfile):
        # Takes a list of records and writes out a formatted output file.
        # Arguments:
            # records_list: list of records utilized in the Avengers class
        with open(outfile, 'w') as ofile:
            ofile.write('# List of the 10 courtries with the highest amount of liters of pure alcohol consumed.\n\n')
            for idx, rc in enumerate(records_list, 1):
                avenger = Avenger(rc)
                
                #Joe F.: I had issues (see Need Help or Slack) with having the '()' 
                # after my dc_characters.something here. May need to remove your 
                # parentheses if you're getting an error about str type not callable, etc.
                ofile.write('## ' + str(idx) + ': ' + avenger.country() + '\n\n')
                ofile.write('* Liters of Beer: ' + avenger.beer_served() + '\n')
                ofile.write('* Liters of Spirit: ' + avenger.spirit_served() + '\n')
                ofile.write('* Liters of Wine: ' + avenger.wine_served() + '\n')
                
                #Joe F.: I would maybe add another '\n' to the end of this to give a space between records?
                ofile.write('* Liters of Pure Alcohol: ' + avenger.total_litres_of_pure_alcohol() + '\n')
