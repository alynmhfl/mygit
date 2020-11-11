import matplotlib.pyplot as plt
import numpy as np

# x and y values 
x = [ 0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]

# Define function which can perform z = x/2 + y. 
z1 = np.array(x) /2 + np.array(y)
z2 = np.array(x2) /2 + np.array(y2)

# Plot bar graph of x, y, x2 and y2.
plt.bar(x, y, label= 'First Line' )
plt.bar(x2, y2, label= 'Second line' ) 

# Plot z1 and z2.
plt.plot(x, z1, label= 'First z', color ='r')
plt.plot(x, z2, label= 'Second z', color = 'g')

# Show x label, y label and graph title.
plt.xlabel( 'Plot Number' )
plt.ylabel( 'Sample Value' )
plt.title( 'Sample Data\n 0 - 100' )

# Show legend and plot. 
plt.legend()
plt.show()

