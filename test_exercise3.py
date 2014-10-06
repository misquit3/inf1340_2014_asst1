

""" Module to test exercise1.py """

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"


#!/usr/bin/env python3
#!/usr/bin/env python3
import pytest

from exercise3 import decide_rps

def test_checksum():
    """
    Inputs that are the correct format and length

    """
       # check that expected input behaves correctly
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Rock") == 1
    # check that correct exception is thrown for unexpected value
    with pytest.raises(ValueError):
        decide_rps("Rock", "Banana") == 1

    # check that correct exception is thrown for bad type
    with pytest.raises(TypeError):
        decide_rps("Rock", 2) == 1





