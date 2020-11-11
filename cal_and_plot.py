import matplotlib.pyplot as plt
import numpy as np

x_array = [ 0 , 1, 2 , 3 ]
y_array = [ 10 , 100 , 50 , 80 ]
x2_array = [ 0 , 1 , 2 , 3 ]
y2_array = [ 100 , 70 , 30 , 30 ]

#define a function which can perform z = x/2 + y. Then plot z.
z = np.array(x_array)/2 + np.array(y_array)
z2 = np.array(x2_array)/2 + np.array(y2_array) 

plt.bar(x_array, y_array, label= 'First Line', color= 'red' )
plt.bar(x2_array, y2_array, label= 'Second Line', color= 'yellow' )
plt.plot(x_array, z, label= 'First Output', color= 'blue' )
plt.plot(x_array, z2, label= 'Second Output', color= 'green' )
plt.xlabel( 'Plot Number' )
plt.ylabel( 'Sample Value' )
plt.title( 'Sample Data\n 0 - 100' )
plt.legend()
plt.show()
