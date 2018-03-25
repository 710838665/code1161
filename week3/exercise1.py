# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    rlist = []
    co = start

    while co < stop:
        rlist.append(co)
        co += 1
    return rlist


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    lr = []

    while start < stop:

        lr.append(start)

        start = start + step

    return lr


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    ralist =[]
    while start < stop:
        ralist.append(start)
        start += 2
    return ralist


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    rl = []
    count = 0

    while start < stop:

        rl.append(start)

        if count % 2:

            start += odd_step

            count += 1

        else:

            start += even_step

            count += 1

    return rl          

def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    while True:


         num = int(input('Enter a num: '))


         if low < num and num < high:


             break


    return num


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    num = None
    while True:
        num = input(message)
        if num.isdigit(): 
            try:
                num = int(num)
                break
    return int(num)
        except ValueError:
            continue
    return num


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    while True:
        number = not_number_rejector('Please enter a number: ')
        if low < number and number < high:
            break
    return number

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
