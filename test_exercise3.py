#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"

# imports one per line
import pytest
from exercise3 import decide_rps


def test_rps():
    """
    check that expected input behaves correctly
    """
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Rock") == 1


def test_value():
    """
    check that correct exception is thrown for unexpected value
    """
    with pytest.raises(ValueError):
        decide_rps("Rock", "Banana")
        decide_rps("asdj", "Papppper")


def test_type():
    """
    check that correct exception is thrown for bad type
    """
    with pytest.raises(TypeError):
        decide_rps(2, "Banana")
        decide_rps("asdj", 2)
        decide_rps("Paper", 2)
