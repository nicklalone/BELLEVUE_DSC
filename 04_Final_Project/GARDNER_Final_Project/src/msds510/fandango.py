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
            self.film_value = record['film']
            self.rottentomatoes_value = record['rottentomatoes']
            self.metacritic_value = record['metacritic']
            self.imdb_value = record['imdb']
            self.fandango_rating_value = record['fandango_ratingvalue']
            self.fandango_votes_value = record['fandango_votes']

    # Method Definitions

    def film(self):
        # Returns the film name
        return self.film_value

    def rotten_tomatoes(self):
        # Returns the Rotten Tomatoes score for the film
        return self.rottentomatoes_value

    def metacritic(self):
        # Returns the MetaCritic score for the film
        return self.metacritic_value

    def imdb(self):
        # Returns the IMDB score for the film
        return self.imdb_value

    def fandango_rating(self):
        # Returns the Fandango score for the film
        return self.fandango_rating_value

    def fandango_votes(self):
        # Returns the number of Fandango votes for the film
        return self.fandango_votes_value

    def __str__(self):
        # Reads the object as a string
        return self.film()

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
            ofile.write('# List of the 10 films with the highest amount of Fandango votes.\n\n')
            for idx, rc in enumerate(records_list, 1):
                avenger = Avenger(rc)
                ofile.write('## ' + str(idx) + ': ' + avenger.film() + '\n\n')
                ofile.write('* Rotten Tomatoes Score: ' + avenger.rotten_tomatoes() + '\n')
                ofile.write('* MetaCritic Score: ' + avenger.metacritic() + '\n')
                ofile.write('* IMDB Score: ' + avenger.imdb() + '\n')
                ofile.write('* Fandango Score: ' + avenger.fandango_rating() + '\n')
                ofile.write('* Number of Fandango Votes: ' + avenger.fandango_votes() + '\n\n\n')
