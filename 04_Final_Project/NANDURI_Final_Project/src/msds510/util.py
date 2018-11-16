
"""
Utility module to differentiate file name and path and return to the calling objects.
Used in convert_to_utf8.py, process_csv.py, make_report.py.
"""


def getfilepath(file):
    """
    Utility function that takes the input arguments that contains file name and path and returns file path
    """

    dirlen = file.rindex('/', 0, len(file))
    dir = file[0:dirlen]
    return dir


def getfilename(file):
    """
    Utility function that takes the input arguments that contains file name and path and returns file name
    """

    dirlen = file.rindex('/', 0, len(file))
    filename = file[dirlen+1: len(file)]
    return filename
