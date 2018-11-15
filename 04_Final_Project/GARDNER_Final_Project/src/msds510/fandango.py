import sys

class Fandango:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.film = record["film"]
            self.rottentomatoes = int(record["rottentomatoes"])
            self.metacritic = int(record["metacritic"])
            self.imdb = float(record["imdb"])
            self.fandango_ratingvalue = float(record["fandango_ratingvalue"])
            self.fandango_votes = int(record["fandango_votes"])



    def get_film(self):
        ''' Returns the film name'''
        return self.film

    def get_rottentomatoes(self):
        ''' Returns the Rotten Tomatoes score'''
        return self.rottentomatoes

    def get_metacritic(self):
        ''' Returns the Metacritic score'''
        return self.metacritic

    def get_imdb(self):
        ''' Returns the IMDB score'''
        return self.imdb

    def get_fandango_ratingvalue(self):
        ''' Returns the Fandango Rating Value'''
        return self.fandango_ratingvalue

    def get_fandango_votes(self):
        ''' Returns the number of Fandango Votes'''
        return self.fandango_votes

    def __str__(self):
        """
        Returns:str: A human-readable value for this biopic
        """
        return self.film()

    def __repr__(self):
        """
        Returns: str: String representation of object.  Useful for debugging.
        """

        return "Fandango(" + ",".join(key + "=" + val
                                     for key, val in self.record.items()
                                     if key == 'film'
                                     or key == 'rottentomatoes') + ")"


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
                fan = Fandango(rc)
                ofile.write('# %d: %s \n\n' % (idx +1, Fandango.get_film(self)))
                ofile.write('* The Rotten Tomatoes score for %d is %s \n' % (Fandango.get_film(self), Fandango.get_rottentomatoes(self)))
                ofile.write('* The MetaCritic score for %d is %s \n' % (Fandango.get_film(self), Fandango.get_metacritic(self)))
                ofile.write('* The IMDB score for %d is %s \n' % (Fandango.get_film(self), Fandango.get_imdb(self)))
                ofile.write('* The Fandango Rating Value for %d is %s \n' % (Fandango.get_film(self), Fandango.get_fandango_ratingvalue(self)))
                ofile.write('* %d had %s votes.\n' % (Fandango.get_film(self), Fandango.get_fandango_votes(self)))

