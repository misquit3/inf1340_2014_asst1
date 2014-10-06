#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"

# imports one per line
import array


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    # LETTER GRADE
    if type(grade) is str:
        # check that the grade is one of the accepted values
        # created a hash-map for easy value look up
        accepted_values = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
                           'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'FZ': 0.0}
        if grade in accepted_values:
            # assign grade to letter_grade based on hash key
            gpa = accepted_values[grade]
        # if grade is not one the accepted values, raise a ValueError
        else:
            raise ValueError('Parameter is out of range')
    # NUMERIC GRADE
    elif type(grade) is int:
        # check that grade is in the accepted range
        if 0 <= grade <= 100:
            if grade >= 85:
                gpa = 4.0
            elif grade >= 80:
                gpa = 3.7
            elif grade >= 77:
                gpa = 3.3
            elif grade >= 73:
                gpa = 3.0
            elif grade >= 70:
                gpa = 2.7
            else:
                gpa = 0.0
        # throw an error if out of accepted range
        else:
            raise ValueError('Parameter is out of range')
    # raise a TypeError exception - if grade is not string or int
    else:
        raise TypeError("Invalid type passed as parameter")
    return gpa
