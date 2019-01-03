"""
Library for dice rolling

"""

import random


def flip_a_coin():
    return random.randint(0,1)

def roll_d4():
    return random.randint(1,4)

def roll_d6():
    return random.randint(1,6)

def roll_d8():
    return random.randint(1,8)

def roll_d10():
    return random.randint(1,10)

def roll_d12():
    return random.randint(1,12)

def roll_n_sided_die(n):
    return random.randint(1,n)

def roll_multiple_n_sided_dice(number_of_dice, n):
    """
    This will roll several n-sided die.  How many dice to roll is
    given by "number_of_dice" and n is the number of sides for
    each die.

    return the total sum of all these dice
    """
    sum = 0
    for i in range(int(number_of_dice)):
        roll = random.randint(1,n)
        sum = sum + roll
    return sum
