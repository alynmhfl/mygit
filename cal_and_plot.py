import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0 , 1, 2, 3]
y2 = [100, 70, 30, 30]

#Define a function which can perform z = x/2 + y. Then plot z.
#Name your file as cal_and_plot.py

def z_plot (a, b):
	z_plot = []
	for count in range (4):
		z_plot.insert(count, a[count]/2 + b[count])
	return z_plot
		
z = (z_plot(x,y))
z2 = (z_plot(x2,y2))

plt.plot(x , z, label = "Plot Z for x and y", color = "black")
plt.plot(x2, z2, label = "Plot Z2 for x2 and y2", color = "red")
plt.bar(x, y, label = 'First Line')
plt.bar(x2, y2, label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel ('Sample Value')
plt.title( 'Sample Data\n 0 - 100')
plt.legend()
plt.show()


