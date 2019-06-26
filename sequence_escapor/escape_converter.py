import sys
from urllib.parse import quote


def converter(string):
    """
    Method to convert a string to an escaped version to input in browsers.
    Has to check if string actually has sufficient length to be converted,
    so that a string like "" would return an error and exit.

    :param string: refers to the string to be converted
    :return: a string in a converted format.
    """
    if len(string) > 0:
        return quote(string)
    else:
        print("Please provide an actual string")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("To run this script, you must provide more than one input.")
        sys.exit(1)
    else:
        print(converter(sys.argv[1]))
