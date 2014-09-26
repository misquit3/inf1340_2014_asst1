#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit (string) universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
        TypeError if string consists of non-numeric characters
    """

    # check type of input
    if type(upc) is str:

        # check length of string
        string_length = len(upc)

        # raise ValueError if not 12
        if string_length != 12:
            # check if length is greater or smaller than 12 and adjust error message
            if string_length > 12:
                error_message = str(string_length - 12) + ' digits over'
            else:
                error_message = str(12 - string_length) + ' digits under'

            raise ValueError('String is the wrong length (' + error_message + ')')
        # upc is exactly 12 characters long
        else:
            # convert string to array
            upc_array = list(upc)
            # convert array of strings to array of ints
            upc_array = convert_to_ints(upc_array)

            """
            generate checksum using the first 11 digits provided
            python arrays are 0 indexed so first position would be 0
            third = index 2 etc.

            [start:end:step]
            want to end at 11 since we do not want to include 12th digit in our calculations
            """
            #add odd-numbered positions
            odd_sum = sum(upc_array[0:11:2])
            #add even-numbered positions
            even_sum = sum(upc_array[1:11:2])

            # check_digit is the 12th digit of UPC
            # do calculations
            check_digit = (odd_sum*3+even_sum)%10
            if check_digit != 0:
                check_digit = 10-check_digit

    # raise TypeError if not string
    else:
        raise TypeError('Parameter is not a string')

    # check UPC against the the 12th digit
    # return True if they are equal, False otherwise
    return check_digit == upc_array[11]


def convert_to_ints(array):
    """
    Converts array of numeric strings to an array of integers
    :param array: list of string digits e.g. ['1','2','3']
    :return: list of ints e.g. [1,2,3]
    :raises: TypeError if any values inside the list cannot be casted to int
    """
    try:
        return [int(value) for value in array]
    except:
        raise TypeError('string consists of non-numeric characters')