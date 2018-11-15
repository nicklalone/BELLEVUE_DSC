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
            self.rottentomatoes = record["rottentomatoes"]
            self.rottentomatoes_user = record["rottentomatoes_user"]
            self.metacritic = record["metacritic"]
            self.metacritic_user = record["metacritic_user"]
            self.imdb = record["imdb"]
            self.fandango_stars = record["fandango_stars"]
            self.fandango_ratingvalue = record["fandango_ratingvalue"]
            self.rt_norm = record["rt_norm"]
            self.rt_user_norm = record["rt_user_norm"]
            self.metacritic_norm = record["metacritic_norm"]
            self.metacritic_user_norm = record["metacritic_user_norm"]
            self.imdb_norm = record["imdb_norm"]
            self.rt_norm_round = record["rt_norm_round"]
            self.rt_user_norm_round = record["rt_user_round"]
            self.metacritic_norm_round = record["metacritic_norm_round"]
            self.metacritic_user_norm_round = record["metacritic_user_norm_round"]
            self.imdb_norm_round = record["imdb_norm_round"]
            self.metacritic_user_vote_count = record["metacritic_user_vote_count"]
            self.imdb_user_vote_count = record["imdb_user_vote_count"]
            self.fandango_votes = record["fandango_votes"]
            self.fandango_difference = record["fandango_difference"]

            '''
            I probably don't need to make a record for each field within the record, but I want to include everything
            first, just in case.
            '''


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
                ofile.write('# ' + str(idx + 1) + '. ' + str(fangango.get_film()) + '\n\n')
                ofile.write('* The Rotten Tomatoes score for ' + str(fandango.get_film()) + 'is ' + str(fandango.get_rottentomatoes()) + '\n')
                ofile.write('* The MetaCritic score for ' + str(fandango.get_film()) + 'is ' + str(fandango.get_metacritic()) + '\n')
                ofile.write('* The IMDB score for ' + str(fandango.get_film()) + 'is ' + str(fandango.get_imdb()) + '\n')
                ofile.write('* The Fandango Rating Value for ' + str(fandango.get_film()) + 'is ' + str(fandango.get_fandango_ratingvalue()) + '\n')
                ofile.write('* ' + str(fandango.get_film()) + ' had ' + str(fandango.get_fandango_votes()) + ' votes.' + '\n')

