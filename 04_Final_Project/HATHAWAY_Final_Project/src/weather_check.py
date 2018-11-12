import datetime


class Weathercheck:
    def __init__(self, record=None):
        """
        Initializes the object with a dictionary-based record. If
        no records is provided, the instance attributes are not set.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """

        if record:
            self.record = record
            self.respondent_id = record["respondentid"]
            self.check_daily_weather = record["do_you_typically_check_a_daily_weather_report"]
            self.how_check_weather = record["how_do_you_typically_check_the_weather"]
            self.website_app = record["a_specific_website_or_app_please_provide_the_answer"]
            self.smartwatch_likely = record["if_you_had_a_smartwatch_like_the_soon_to_be_released_apple_watch_how_likely_or_unlikely_would_you_be_to_check_the_weather_on_that_device"]
            self.age = record["age"]
            self.gender = record["what_is_your_gender"]
            self.combined_money_household = record["how_much_total_combined_money_did_all_members_of_your_household_earn_last_year"]
            self.us_region = record["us_region"]

    def check_daily(self,recordslist):
        """

        Returns:
            int: count of how many respondents check the weather daily

        """
        count = 0
        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.check_daily_weather == 'True':
                count +=1

        return count


    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file.
        Args:
            recordslist: list of respondents somewhat or very likely to check weather on Smartwatch
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """


        #with open(outfile, 'w') as ofile:
        #for idx, rc in enumerate(recordslist):


                #ofile.write("# %d %s\n" %(idx+1, avenger.name_alias()) )
        weather = Weathercheck()
        print("Number of people who check weather daily %d " % weather.check_daily(recordslist))

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
