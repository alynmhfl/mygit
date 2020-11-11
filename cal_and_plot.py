import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([ 0, 1, 2, 3 ])
y1 = np.array([ 10, 100, 50, 80 ])
x2 = np.array([ 0, 1, 2, 3 ])
y2 = np.array([ 100, 70, 30, 30 ])
z1 = x1/2 + y1
z2 = x2/2 + y2

# Define a function which can perform z = x/2 + y. Then plot z.
# Name youe file as cal_and_plot.py

plt.bar(x1, y1, color = 'yellow', label = 'First Line')
plt.bar(x2, y2, color = 'green', label = 'Second Line')
plt.plot(x1, z1, color = 'blue', label = 'First Output')
plt.plot(x2, z2, color = 'red', label = 'Second Output')
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data\n 0 - 100')
plt.legend()
plt.show()
