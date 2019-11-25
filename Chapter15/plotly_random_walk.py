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

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        return self.x_values, self.y_values


import os

os.chdir(os.path.dirname(__file__))

rw = RandomWalk()
x_values, y_values = rw.fill_walk()


import plotly.graph_objects as go
from plotly import offline

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = x_values,
    y = y_values,
    mode='lines+markers',
    marker=dict(
        size=5,
        color=list(range(len(x_values))), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=False
    )
))

fig.add_trace(go.Scatter(
    x = [x_values[0]],
    y = [y_values[0]],
    mode='markers',
    marker=dict(
        size=15,
        color='green'
    )
))

fig.add_trace(go.Scatter(
    x = [x_values[-1]],
    y = [y_values[-1]],
    mode='markers',
    marker=dict(
        size=15,
        color='red'
    )
))


offline.plot(fig, filename='d6.html')

