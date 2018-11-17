class Fifa:
    def __init__(self, record=None):

        if record:
            self.record = record
            self.country_name = record["country"]
            self.confederation_name = record["confederation"]
            self.population_share_value = record["population_share"]
            self.tv_audience_share_value = record["tv_audience_share"]
            self.gdp_weighted_share_value = record["gdp_weighted_share"]

    def country(self):

        return self.country_name

    def confederation(self):

        return self.confederation_name

    def population_share(self):

        return float(self.population_share_value)

    def tv_audience_share(self):

        return float(self.tv_audience_share_value)

    def gdp_weighted_share(self):

        return float(self.gdp_weighted_share_value)

    def __str__(self):

        return self.country()

    def __repr__(self):

        return "Fifa(" + ",".join(key + "=" + val
                                  for key, val in self.record.items()
                                  if key == 'country'
                                  or key == 'confederation') + ")"

    def to_markdown(self, recordslist, outfile):

        with open(outfile, 'w') as ofile:
            for idx, rc in enumerate(recordslist):
                fifa = Fifa(rc)
                ofile.write("# " + str(idx + 1) + ". " + fifa.country() + "\n\n")

                ofile.write("* Confederation: " + fifa.confederation() + "\n")

                ofile.write("* Population Share: " + str(fifa.population_share()) + "\n")

                ofile.write("* TV Audience Share: " + str(fifa.tv_audience_share()) + "\n")

                ofile.write("* GDP Weighted Share: " + str(fifa.gdp_weighted_share()) + "\n\n")

                #               ofile.write('# {}{} {}'.format(idx, ".", avenger.name_alias()))

                # ofile.write('\n\n* {} {}'.format('Country: ', avenger.country()))

                # ofile.write('\n* {} {}'.format('Confederation: ', avenger.confederation()))

                # ofile.write('\n* {} {}'.format('Population Share: ', avenger.population_share()))

                # ofile.write('\n* {} {}'.format('TV Audience Share: ', avenger.tv_audience_share))

                # ofile.write('\n* {} {}'.format('GDP Weighted Share: ', avenger.gdp_weighted_share))

                # ofile.write('\n\n## {}'.format("Notes"))

                # ofile.write('\n\n{}\n\n'.format(avenger.notes()))
