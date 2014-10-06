#!/usr/bin/env python3

"""
#!/usr/bin/env python3

    Decide the result of a rock, paper, scissors game

    Assignment 1, Exercise 3, INF1340 Fall 2014

    ------------------------------
    Let
    ------------------------------
        rock     = 0
        paper    = 1
        scissors = 2
    ------------------------------
    Player 1    Player 2    result
    ------------------------------
       0           0           0
       0           1           2
       0           2           1

       1           0           1
       1           1           0
       1           2           2

       2           0           2
       2           1           1
       2           2           0

    ------------------------------
    result = (player1-player2)%3
    ------------------------------
"""

__author__ = 'Joanna Kolbe, Tania Misquitta'
__email__ = "joannakolbe@gmail.com"
__copyright__ = "2014 JK, TM"
__status__ = "Prototype"


def decide_rps(player1, player2):
    """
    Returns the winner of rock-paper-scissors game.

    :param:
        player1 (string): choice of rock, paper or scissors
        player2 (string) choice of rock, paper or scissors
            Does not matter if it's upper or lower case, as long as it
            consists of the proper letter sequence
            e.g. 'Rock', 'scissors', 'pApEr', 'ROCK', etc.

    :return:
        int: winner of the game
                0 -> tie
                1 -> player1 wins
                2 -> player2 wins

    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is not one of possible choices
    """

    if type(player1) is str and type(player2) is str:

        # convert to lower case so the user may words in upper case as well
        player1 = player1.lower()
        player2 = player2.lower()

        #hash-map to match string values to their int representations
        option_map = {'rock': 0, 'paper': 1, 'scissors': 2}

        #check if parameters are one of the possible choices
        if player1 in option_map and player2 in option_map:
            """
            everything is correct, perform mapping and calculations
            the results is (player1 - player2)%3
                e.g. player1 -> scissors = 2
                     player2 -> paper = 1
                     (2-1)%3 = 1%3 = 1 (player 1 wins)
            """
            retval = (option_map[player1] - option_map[player2]) % 3

            return retval


        #one or both parameters are not one of the options e.g. 'hammer'
        else:
            raise ValueError('not a valid string value')

    # parameters are not strings
    else:
        raise TypeError('Parameter is not a string')