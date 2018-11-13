# Fundamentally re-written for bad drivers.
from googlesearch import search

# DO NOT EDIT THE FORMATTING IN THIS FILE!!! NO EXTRA CR AND WHITE SPACE!!!

class BadDrivers:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        if record:
            self.record = record
            self.state = record["state"]
            self.fatal_collisions = record["number_of_drivers_involved_in_fatal_collisions_per_billion_miles"]
            self.speeding = record["percentage_of_drivers_involved_in_fatal_collisions_who_were_speeding"]
            self.drunk = record["percentage_of_drivers_involved_in_fatal_collisions_who_were_alcohol-impaired"]
            self.not_distracted = record["percentage_of_drivers_involved_in_fatal_collisions_who_were_not_distracted"]
            self.no_priors = record["percentage_of_drivers_involved_in_fatal_collisions_who_had_not_been_involved_in_any_previous_accidents"]
            self.premiums = record["car_insurance_premiums_($)"]
            self.losses = record["losses_incurred_by_insurance_companies_for_collisions_per_insured_driver_($)"]

    def get_state(self):
        """
        Returns:
            str: Driver's state
        """
        return self.state

    def get_fatal_collisions(self):
        """
        Returns:
            float: The # driver involved in fatal collisions per billion miles
        """
        return self.fatal_collisions

    def get_speeding(self):
        """
        Returns:
            int: % drivers in fatal accidents while speeding
        """
        return self.speeding

    def get_drunk(self):
        """
        Returns:
            int: The number of comic books that character
            appeared in as of April 30
        """
        return self.drunk

    def get_not_distracted(self):
        """
        Returns:
            int: % drivers in fatal accidents who were not distracted
        """
        return self.not_distracted

    def get_no_priors(self):
        """
        Returns:
            int: % of drivers in fatal accidents without prior accidents
        """
        return self.no_priors

    def get_premiums(self):
        """
        Returns:
            float: The premium the driver paid
        """
        return self.premiums

    def get_losses(self):
        """
        Returns:
            float: Insured losses per collision per driver
        """
        return self.losses

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of top 10 bad driver records
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """
        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                # Instantiate the BadDrivers object
                bad_drivers = BadDrivers(rc)
                # Do stuff with it - specifically, print each element to the .md file
                ofile.write("# " + str(idx + 1) + ". " + bad_drivers.get_state() + "\n\n")
                ofile.write("* Number of fatals per billion miles: " + str(bad_drivers.get_fatal_collisions()) + "\n")
                ofile.write("* % fatals while driver speeding: " + str(bad_drivers.get_speeding()) + "\n")
                ofile.write("* % fatals while driver drunk: " + str(bad_drivers.get_drunk()) + "\n")
                ofile.write("* % fatals while driver NOT distracted: " + str(bad_drivers.get_not_distracted()) + "\n")
                ofile.write("* % fatals while drivers had no priors: " + str(bad_drivers.get_no_priors()) + "\n")
                ofile.write("* Premium for bad driver: " + '$' + str(bad_drivers.get_premiums()) + "\n")
                ofile.write("* Losses per collision per driver: " + str(bad_drivers.get_losses()) + "\n")

            # Now that the driver record information is printed, list some stuff from Google on bad drivers.
            ofile.write('## Google search. Warning: some content may be inappropriate.' + '\n')
            ofile.write('Now that you have seen bad drivers per state, let\'s look at actual bad drivers.' + '\n')
            for google_result in search('Bad Drivers', tld='com', num=10, stop=1, pause=2):
                ofile.write('* ' + google_result + '\n')



