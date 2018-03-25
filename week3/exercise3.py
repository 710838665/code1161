"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division

from __future__ import print_function

from exercise1 import not_number_rejector

from exercise1 import super_asker

import random


def advancedGuessingGame():
    """
    """
    print("A number between _ and _ ?")



    ln = not_number_rejector("Please give a lower number: ")



    while True:

        un = not_number_rejector("Please give an upper number: ")



    print("And, a number between {} and {} ?".format(ln,un))
    ac = random.randint(ln, un)
    print (ac)
    guessed = False

    while not guessed:

        guessedNumber = super_asker(ln, un)

        print("you guessed {},".format(guessedNumber))

        if guessedNumber not in range(ln, un + 1):

            print("The gussed number is not between {} and {}."

                  .format(ln, un))

        elif guessedNumber == ac:

            print("you got it!! It was {}".format(ac))

            guessed = True

        elif guessedNumber < ac:

            print("too small, try again ")

        else:

            print("too big, try again   ")

        return "You got it!"

  

if __name__ == "__main__":
    advancedGuessingGame()
