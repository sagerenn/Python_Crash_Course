import matplotlib.pyplot as plt 

from random import randint

class Dice:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Assume a six-sided dice"""
        self.sides = sides

    def roll_dice(self):
        """roll a dice to generate number from 1 to number of sides"""
        return randint(1, self.sides)

def multi_dices(dice_sides, roll_times=100000):
    """simulate roll the number of different sides of dices"""

    max_result = 0

    tmp_dict = {}
    for index in range(len(dice_sides)):
        max_result += dice_sides[index]
        tmp_dict[index] = Dice(dice_sides[index])

    results = []
    while len(results) < roll_times:
        tmp_result = 0
        for index in range(len(dice_sides)):
            tmp_result += tmp_dict[index].roll_dice()
        results.append(tmp_result)

    min_result = len(dice_sides)

    frequencies = \
        [ results.count(value) for value in range(min_result, max_result+1) ]


    return list(range(min_result, max_result+1)), frequencies

import os

os.chdir(os.path.dirname(__file__))


x_values, y_values = multi_dices([6,8])

fig, ax = plt.subplots()
plt.bar(x_values, y_values)

plt.xticks(x_values)

plt.savefig("test.png", bbox_inches='tight')

