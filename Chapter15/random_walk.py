from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """get the random step of one axis"""
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk"""

        while len(self.x_values) < self.num_points:
            # # x_direction = choice([1, -1])
            # x_direction = choice([1])
            # # x_distance = choice([0,1,2,3,4])
            # x_distance = choice([0,1,2,3,4,5,6,7,8])
            # x_step = x_direction * x_distance

            # # y_direction = choice([1, -1])
            # y_direction = choice([1])
            # # y_distance = choice([0,1,2,3,4])
            # y_distance = choice([0,1,2,3,4,5,6,7,8])
            # y_step = y_direction * y_distance

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        return self.x_values, self.y_values


import matplotlib.pyplot as plt
import os
import time

os.chdir(os.path.dirname(__file__))

# while True:
rw = RandomWalk(50_000)
x_list, y_list = rw.fill_walk()

plt.style.use('seaborn')

fig, ax = plt.subplots(figsize=(15, 9), dpi=300)
# ax.scatter(x_list, y_list, c=range(rw.num_points), edgecolors='none',
#         cmap=plt.cm.Blues, s=1)
ax.plot(x_list, y_list, linewidth=1)
ax.scatter(x_list[0], y_list[0], c='green', edgecolors='none', s=100)
ax.scatter(x_list[-1], y_list[-1], c='red', edgecolors='none', s=200)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('test.png', bbox_inches='tight')
    # time.sleep(5)