import matplotlib.pyplot as plt

x = [ 0, 1, 2, 3 ]
y = [ 10, 100, 50, 80 ]
x2 = [ 0, 1, 2, 3 ]
y2 = [ 100, 70, 30, 30 ]

# define a function which can perform z = x/2 + y. Then plot z.
# Name your file as cal_and_plot.py

def Z(x,y):
	z = []
	for count in range(4):
		z.insert(count, x[count]/2 + y[count])
	return z

z = (Z(x,y))
z2 = (Z(x2,y2))

plt.plot(x, z, color = 'brown', label= 'z')
plt.plot(x2, z2, color = 'purple', label= 'z2')
plt.bar(x, y, label= 'First Line')
plt.bar(x2, y2, label= 'Second Line')
plt.xlabel( 'Plot Number' )
plt.ylabel( 'Sample Value' )
plt.title( 'Sample Data\n 0-100' )
plt.legend()
plt.show()
