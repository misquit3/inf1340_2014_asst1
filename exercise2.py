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

            # generate checksum using the first 11 digits provided

            #add odd-numbered positions
            #python arrays are 0 indexed so first position would be 0
            #third = index 2 etc.

            odd_sum = sum(upc_array[0:11:2])
            even_sum = sum(upc_array[1:11:2])

            check_digit = (odd_sum*3+even_sum)%10
            if check_digit != 0:
                check_digit=10-check_digit

    # raise TypeError if not string
    else:
        raise TypeError('Parameter is not a string')

    # check against the the twelfth digit
    # return True if they are equal, False otherwise
    if check_digit == upc_array[11]:
        return True
    else:
        return False


def convert_to_ints(array):
    try:
        return [int(value) for value in array]
    except:
        raise TypeError('UPC contains not allowed characters')