#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
    with pytest.raises(TypeError):
        checksum(786936224306)

    with pytest.raises(ValueError):
        checksum("1")
    with pytest.raises(ValueError):
        checksum("1234567890")

        # other tests


# add functions for any other tests
def test_format():
    """
    Inputs that consist incorrect non-numeric characters
    """
    with pytest.raises(TypeError):
        checksum("123x56789!12")
    with pytest.raises(TypeError):
        checksum("x23356789312")
    with pytest.raises(TypeError):
        checksum("x233567@o312")
