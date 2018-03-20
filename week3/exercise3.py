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
    print("\nwelcome to the guessing game!")
    print("A number between 10 and 20 ?")

    actualNumber = random.randint(10, 20)

    guessed = False
    word = [11, 12, 13, 14, 15, 16, 17, 18, 19]

    while not guessed:
        guessedNumber = int(input("guess a number: "))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber = word:
            print("good")5
        elif guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
           
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        elif guessedNumber > actualNumber:
            print("too big, try again   ")
        else:
            print("try again")    
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
