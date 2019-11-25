import os
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(__file__))

# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# input_values = range(1,1001)
# squares = [x**2 for x in input_values]
input_values = range(-3000,3001)
squares = [x**3 for x in input_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

# ax.scatter(input_values, squares, c='red', s=100)
# ax.scatter(input_values, squares, c=(0, 0.8, 0), s=100)
# ax.scatter(input_values, squares, c=input_values, cmap=plt.cm.Blues, s=100)
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=100)

ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='x', which='major', labelsize=10)
# ax.axis([0,1100,0,1500000])

plt.savefig("test.png", bbox_inches='tight')

