"""represent a dice"""

from random import randint

class Dice():
    """model a dice"""

    def __init__(self, sides=6):
        """initialize a instance of dice"""
        self.sides = sides

    def roll_dice(self):
        """roll the dice to generate randomly the number from 1 to sides"""
        return randint(1, self.sides)