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
            self.income = record["how_much_total_combined_money_did_all_members_of_your_household_earn_last_year"]
            self.us_region = record["us_region"]

    def check_daily(self,recordslist):
        """
        Takes a list of records and counts the number of respondents
        that check teh weather daily
        Returns:
            int: count of how many respondents check the weather daily

        """
        count = 0
        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.check_daily_weather == 'True':
                count +=1

        return count

    def age_brackets(self,recordslist):
        """
        takes a list of records and counts the number of respondents
        in each bracket of age ranges
        :param recordslist:
        :return: number of respondents in each age bracket
        """

        age18_29 = 0
        age30_44 = 0
        age45_59 = 0
        age_over_60 = 0
        no_age_given = 0

        # NRR comment: I like the below usage looping concept for grouping by age. Its quite handy.
        # Nishi comment - The looping done below is very concise and efficiently done. 

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.age == "18 - 29":
                age18_29 +=1
            elif weather.age == "30 - 44":
                age30_44 +=1
            elif weather.age == "45 - 59":
                age45_59 +=1
            elif weather.age == "60+":
                age_over_60 +=1
            else:
                no_age_given +=1

        return {"18 - 29":age18_29, "30 - 44":age30_44, "45 - 59":age45_59, "60+":age_over_60, "Not given":no_age_given}

    def how_check(self, recordslist):
        """
        sums for each type, number of respondents that check weather on different media
        :param recordslist:
        :return: number of respondents in each category
        """
        website = 0
        internet = 0
        tv = 0
        newsletter = 0
        newspaper = 0
        radio = 0
        weather_app = 0
        weather_channel = 0
        no_answer = 0

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.how_check_weather == "A specific website or app (please provide the answer)":
                website += 1
            elif weather.how_check_weather == "Internet search":
                internet += 1
            elif weather.how_check_weather == "Local TV News":
                tv += 1
            elif weather.how_check_weather == "Newsletter":
                newsletter += 1
            elif weather.how_check_weather  == "Newspaper":
                newspaper += 1
            elif weather.how_check_weather == "Radio weather":
                radio += 1
            elif weather.how_check_weather == "The default weather app on your phone":
                weather_app += 1
            elif weather.how_check_weather == "The Weather Channel":
                weather_channel += 1
            else: no_answer += 1

        return {"A specific website or app (please provide the answer)": website, "Internet search": internet, "Local TV News": tv, "Newsletter": newsletter, "Newspaper": newspaper, "Radio weather": radio, "The default weather app on your phone": weather_app, "The Weather Channel": weather_channel }

    def gender_id(self, recordslist):
        """
        categoriges respondents by male or female
        :param recordslist:
        :return: returns count of male and female respondents
        """

        male = 0
        female = 0
        none = 0

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.gender == "Male":
                male += 1
            elif weather.gender == "Female":
                female += 1
            else: none += 1
        return {"The number of men responding were ": male, "The number of women responding were ": female, none: "chose not to respond "}

    def region(self, recordslist):
        """
        categorizes respondents by the region of the US where they reside
        :param self:
        :param recordlist:
        :return: count of respondents by region
        """

        central = 0
        west = 0
        east_coast = 0
        none = 0

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.us_region == "East North Central" or weather.us_region == "East South Central" or weather.us_region == "West North Central" or weather.us_region == "West South Central":
                central += 1
            elif weather.us_region == "Middle Atlantic" or weather.us_region == "South Atlantic" or weather.us_region == "New England":
                east_coast += 1
            elif weather.us_region == "Mountain" or weather.us_region == "Pacific":
                west += 1
            else: none +=1

        return {"Central US respondents": central, "West Coast respondents": west, "East Coast respondents": east_coast, "No region given": none}

    def household_income(self, recordslist):
        """
        ategorizes respondents by income range
        :param recordslist:
        :return: count of respondents by income bracket
        """
        inc0_49 = 0
        inc50_99 = 0
        inc100_149 = 0
        inc150_199 = 0
        inc200_up = 0
        inc_no_answer = 0

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            if weather.income == "$0 to $9,999" or weather.income == "$10,000 to $24,999" or weather.income == "$25,000 to $49,999":
                inc0_49 +=1
            elif weather.income == "$50,000 to $74,999" or weather.income == "$75,000 to $99,999":
                inc50_99 +=1
            elif weather.income == "$100,000 to $124,999" or weather.income == "$125,000 to $149,999":
                inc100_149 +=1
            elif weather.income == "$150,000 to $174,999" or weather.income == "$175,000 to $199,999":
                inc150_199 +=1
            elif weather.income == "$200,000 and up":
                inc200_up +=1
            else: inc_no_answer +=1

        return {"$0 to $49,999": inc0_49, "$50,000 to $99,999": inc50_99, "$100,000 to $149,999": inc100_149, "$150,000 to $199,999": inc150_199, "$200,000 and above": inc200_up, "Preferred not to answer or gave no answer": inc_no_answer}

    def respondents(self, recordslist):
        """
		Takes a list and counts the number of respondents in list
	    :param: recordslist
	    :return: count of respondents to survey
	    """

        count = 0

        for idx, rc in enumerate(recordslist):
            weather = Weathercheck(rc)
            count += 1

        return count

    def to_markdown(self, recordslist, outfile):
        """takes a list of records, formats them
        and prints them to an output file in markdown.
        Args:
            recordslist: list of respondents somewhat or very likely to check weather on Smartwatch
            outfile: a file location string.
        Result:
            prints the contents to a formatted outfile.
        """

        weather = Weathercheck()
        with open(outfile, 'w') as ofile:
            ofile.write("# Survey Results for People Likely to Check the Weather on a Smartwatch\n")
            ofile.write("## There were {} respondents who were somewhat likely or very likely to use a smartwatch to check the weather\n" .format(weather.respondents(recordslist)))
            ofile.write("## There were {} respondents who check the weather daily\n" .format(weather.check_daily(recordslist)))
            ofile.write("## Number of Respondents Using Various Methods to Check the Weather:\n")
            for k, v in weather.how_check(recordslist).items():
                ofile.write("* {0}: {1}\n" .format(k, v))
            ofile.write("## Number of Respondents in Each Age Bracket:\n")
            # DHULIPALA: Really interesting the way you incorporated a method that gives a dictionary directly making the code very precise
            for k, v in weather.age_brackets(recordslist).items():
                ofile.write("* {0}: {1}\n" .format(k, v))
            ofile.write("## Number of Respondents in Each Region of the US\n")
            for k, v in weather.region(recordslist).items():
                ofile.write("* {0}: {1}\n" .format(k, v))
            ofile.write("## Number of Respondents in Each Income Bracket:\n")
            for k, v in weather.household_income(recordslist).items():
                ofile.write("* {0}: {1}\n" .format(k, v))
            ofile.write("## Number of Respondents by Gender:\n")
            for k, v in weather.gender_id(recordslist).items():
                ofile.write("* {0} {1}\n" .format(k,v))
