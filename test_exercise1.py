


""" Module to test exercise1.py """

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"


def test_letter_grade():
    """
    Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0, "test letter: Case 1"
    assert grade_to_gpa("A") == 4.0, "test letter: Case 2"
    assert grade_to_gpa("A-") == 3.7, "test letter: Case 3"
    assert grade_to_gpa("B+") == 3.3, "test letter: Case 4"
    assert grade_to_gpa("B") == 3.0, "test letter: Case 5"
    assert grade_to_gpa("B-") == 2.7, "test letter: Case 6"
    assert grade_to_gpa("FZ") == 0.0, "test letter: Case 7"

    with pytest.raises(ValueError):
        grade_to_gpa("q")
    # add more tests for invalid values

def test_percentage_grade():
    """
    Numeric grade inputs
    """
    assert grade_to_gpa(100) == 4.0, "test letter: Case 1"
    assert grade_to_gpa(95) == 4.0, "test letter: Case 2"
    assert grade_to_gpa(90) == 4.0, "test letter: Case 3"

    assert grade_to_gpa(89) == 4.0, "test letter: Case 4"
    assert grade_to_gpa(87) == 4.0, "test letter: Case 5"
    assert grade_to_gpa(85) == 4.0, "test letter: Case 6"

    assert grade_to_gpa(84) == 3.7, "test letter: Case 7"
    assert grade_to_gpa(82) == 3.7, "test letter: Case 8"
    assert grade_to_gpa(80) == 3.7, "test letter: Case 9"

    assert grade_to_gpa(79) == 3.3, "test letter: Case 10"
    assert grade_to_gpa(78) == 3.3, "test letter: Case 11"
    assert grade_to_gpa(77) == 3.3, "test letter: Case 12"

    assert grade_to_gpa(76) == 3.0, "test letter: Case 13"
    assert grade_to_gpa(74) == 3.0, "test letter: Case 14"
    assert grade_to_gpa(73) == 3.0, "test letter: Case 15"

    assert grade_to_gpa(72) == 2.7, "test letter: Case 16"
    assert grade_to_gpa(71) == 2.7, "test letter: Case 17"
    assert grade_to_gpa(70) == 2.7, "test letter: Case 18"

    assert grade_to_gpa(69) == 0.0, "test letter: Case 19"
    assert grade_to_gpa(37) == 0.0, "test letter: Case 20"
    assert grade_to_gpa(0) == 0.0, "test letter: Case 21"

    with pytest.raises(ValueError):
        grade_to_gpa(101)
        grade_to_gpa(-1)


def test_float_input():
    """
    Float inputs
    """
    with pytest.raises(TypeError):
        grade_to_gpa(82.5)

# add functions for any other tests

# imports one per line
import pytest

from exercise1 import grade_to_gpa

grade = input("Enter Grade: ")
if grade.isdigit():
    grade = int(grade)
    print(grade_to_gpa(grade))
else:
    print(grade_to_gpa(grade))
test_float_input()
test_letter_grade()
test_percentage_grade()