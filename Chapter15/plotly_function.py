from random import randint

class Dice:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Assume a six-sided dice"""
        self.sides = sides

    def roll_dice(self):
        """roll a dice to generate number from 1 to number of sides"""
        return randint(1, self.sides)

def six_side_dices(dice_side='6', dice_num='1', roll_times=100000):
    """simulate roll the number of six-sides dices"""

    # create a six-side dice
    dice_6 = Dice(dice_side)

    # Make some roll, and store results in a list
    results = []
    for roll_num in range(roll_times):
        j = 1

        for i in range(dice_num):
            j *= dice_6.roll_dice()

        results.append(j)

    frequencies = []
    x_values = []

    # for value in range(dice_num*1, (dice_num*dice_6.sides)+1):
    for value in results:
        if value not in x_values:
            x_values.append(value)
        else:
            continue
        frequency = results.count(x_values[-1])
        frequencies.append(frequency)
    # return list(range(dice_num*1, (dice_num*dice_6.sides)+1)), frequencies
    return x_values, frequencies

    # frequencies = {
    #     '1': 0,
    #     '2': 0,
    #     '3': 0,
    #     '4': 0,
    #     '5': 0,
    #     '6': 0,
    # }
    # for value in results:
    #     frequencies[str(value)] += 1

    # print(frequencies)

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



from plotly.graph_objs import Bar, Layout
from plotly import offline
import os

os.chdir(os.path.dirname(__file__))


# x_values, frequencies = six_side_dices(6,2,100000)

x_values, frequencies = multi_dices([6,10,10])


data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title=f'Result of rolling', 
        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

