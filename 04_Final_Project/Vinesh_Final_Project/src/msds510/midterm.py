import datetime


class Midterm:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """


        if record:
            self.record = record
            self.party_val = record["party"]
            self.candidate_val = record["candidate"]
            self.state_val = record["state"]
            self.model = record["model"]
            self.incumbent_val = record["incumbent"]
            self.special  = record["special"]
            self.forecastdate = record["forecastdate"]
            self.win_probability_val = record["win_probability"]
            self.voteshare_val = record["voteshare"]
            self.category = record["class"]
            self.p10_voteshare = record["p10_voteshare"]
            self.p90_voteshare = record["p90_voteshare"]

    def party(self):

        return str(self.party_val)

    def candidate(self):

        return str(self.candidate_val)

    def state(self):

        return str(self.state_val)

    def model(self):

            return self.model

    def incumbent(self):

        return self.incumbent_val

    def special(self):
        return self.special

    def forecastdate(self):

        return self.forecastdate

    def win_probability(self):

        return self.win_probability_val

    def voteshare(self):

        return self.voteshare_val

    def category(self):

        return self.category

    def p10_voteshare(self):

        return self.p10_voteshare

    def p90_voteshare(self):

        return self.p90_voteshare


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
            count = 0
            label = ""
            for idx, rc in enumerate(recordslist):
                midterm = Midterm(rc)
                # DHULIPALA: Need to take out the colon
                count = idx+1;
                abc=""+str(count)
                if midterm.party() == "D":
                    ofile.write("# " + abc + " Democrat:" + midterm.party() + "\n")
                elif midterm.party() == "R":
                    ofile.write("# " + abc + " Republican:" + midterm.party() + "\n")
                else:
                    ofile.write("# " + abc + " Independent:" + midterm.party() + "\n")

                ofile.write("* Candidate:  " + midterm.candidate() + "\n")
                ofile.write("* State:  " + midterm.state() + "\n")
                ofile.write("* Win Probability:  " + str(midterm.win_probability()) + "\n")
                ofile.write("* Vote Share:  " + str(midterm.voteshare()) + "\n")
                ofile.write("* Incumbent :  " + str(midterm.incumbent()) + "\n")
                ofile.write("\n\n")

