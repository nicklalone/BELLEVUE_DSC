class Avenger:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.respondentid = record["respondentid"]
            self.consider = record["consider"]
            self.cigarettes = record["do_you_ever_smoke_cigarettes"]
            self.alcohol = record["do_you_ever_drink_alcohol"]
            self.gamble = record["do_you_ever_gamble"]
            self.skydiving = record["have_you_ever_been_skydiving"]
            self.speed = record["do_you_ever_drive_above_the_speed_limit"]
            self.cheated = record["have_you_ever_cheated_on_your_significant_other"]
            self.eat_steak = record["do_you_eat_steak"]
            self.steak_temp = record["how_do_you_like_your_steak_prepared"]
            self.gender = record["gender"]
            self.age = record["age"]
            self.household_income = record["household_income"]
            self.education = record["education"]
            self.location = record["location"]

    def respondentid(self):
        return int(self.respondentid)

    def consider(self):
        return self.consider

    def cigarettes(self):
        return self.cigarettes

    def alcohol(self):
        return self.alcohol

    def gamble(self):
        return self.gamble

    def skydiving(self):
        return self.skydiving

    def speed(self):
        return self.speed

    def cheated(self):
        return self.cheated

    def eat_steak(self):
        return self.eat_steak

    def steak_temp(self):
        return self.steak_temp

    def gender(self):
        return self.gender

    def age(self):
        return self.age

    def household_income(self):
        return self.household_income

    def education(self):
        return self.education

    def location(self):
        return self.location

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
                avenger = Avenger(rc)
                ofile.write('# ' + str(idx + 1) + '. Respondent ID #' + avenger.respondentid + '\n\n')
                ofile.write('* Choice of lottery: ' + str(avenger.consider) + '\n')
                ofile.write('* Smoker: ' + str(avenger.cigarettes) + '\n')
                ofile.write('* Drinker: ' + str(avenger.alcohol) + '\n')
                ofile.write('* Gambler: ' + avenger.gamble + '\n')
                ofile.write('* Skydiver: ' + str(avenger.skydiving + '\n'))
                ofile.write('* Speeder: ' + avenger.speed + '\n')
                ofile.write('* Cheater: ' + avenger.cheated + '\n')
                ofile.write('* Steak Eater: ' + avenger.eat_steak + '\n')
                ofile.write('* Temperature of Steak: ' + avenger.steak_temp + '\n')
                ofile.write('* Gender: ' + avenger.gender + '\n')
                ofile.write('* Age Group: ' + avenger.age + '\n')
                ofile.write('* Household Income: ' + avenger.household_income + '\n')
                ofile.write('* Education: ' + avenger.education + '\n')
                ofile.write('* Region: ' + avenger.location + '\n\n')


