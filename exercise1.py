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

    if type(grade) is str:
        print("letter")  # remove this line once the code is implemented

        # check that the grade is one of the accepted values
        accepted_values = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'FZ']
        if grade in accepted_values:
            # assign grade to letter_grade
            if grade == 'A+' or grade == 'A':
                gpa = 4.0
            elif grade == 'A-':
                gpa = 3.7
            elif grade == 'B+':
                gpa = 3.3
            elif grade == 'B':
                gpa = 3.0
            elif grade == 'B-':
                gpa = 2.7
            else:
                gpa = 0.0
        else:
            raise ValueError('Parameter is out of range')

    elif type(grade) is int:
        # check that grade is in the accepted range
        if 0 <= grade <= 100:
            # convert the numeric grade to a letter grade
            letter_grade = mark_to_letter(grade)
            # assign the value to letter_grade
            gpa = grade_to_gpa(letter_grade)
         # throw an error if out of accepted range
        else:
            raise ValueError('Parameter is out of range')
    else:
        # raise a TypeError exception - if grade is not string or int
        raise TypeError("Invalid type passed as parameter")

    return gpa


def mark_to_letter(mark):
    """
    Returns letter grade corresponding to mark.
    NOTE: range checking is done inside of the grade_to_gpa function!
    :param: mark (int): mark to be converted
    :return: string: Letter grade (Value is in range A+ -> FZ)
    :raises: TypeError if parameter is not an int
    """
    # check if type of passed parameter is correct
    if type(mark) is int:
        if 90 <= mark <= 100:
            letter_grade = "A+"
        elif 85 <= mark <= 89:
            letter_grade = "A"
        elif 80 <= mark <= 84:
            letter_grade = "A-"
        elif 77 <= mark <= 79:
            letter_grade = "B+"
        elif 73 <= mark <= 76:
            letter_grade = "B"
        elif 70 <= mark <= 72:
            letter_grade = "B-"
        else:
            letter_grade = "FZ"
        return letter_grade
    else:
        raise TypeError('Parameter is not an int')



