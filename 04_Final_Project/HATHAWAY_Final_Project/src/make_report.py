import sys
import csv

from weather_check import Weathercheck

def main():
    """interprets command line request
    Args:
        argv: an array with input and output files

    Returns:
        no return. Executed generateReport with
        collected file names.
    """
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        generateReport(sys.argv[1], sys.argv[2])


def generateReport(infile, outfile):
    """reads an infile, sorts the content, and
       sends the sorted records and an outfile
       destination to printMarkdown to print
    Args:
        infile: a file location to read data from
        outfile: a destination file location
    Result:
        executes the printMarkdown function with
        sorted records and an outfile to write
        the results to.
    """

    file = []
    with open(infile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)


    likelyList = []
    for item in file:
        if (item['if_you_had_a_smartwatch_like_the_soon_to_be_released_apple_watch_how_likely_or_unlikely_would_you_be_to_check_the_weather_on_that_device'] == 'Very likely'
                or item['if_you_had_a_smartwatch_like_the_soon_to_be_released_apple_watch_how_likely_or_unlikely_would_you_be_to_check_the_weather_on_that_device']== 'Somewhat likely'):
            likelyList.append(item)

    weather = Weathercheck()
    weather.to_markdown(likelyList, outfile)

if __name__ == '__main__':
    main()
