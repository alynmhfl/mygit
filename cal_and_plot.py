import matplotlib.pyplot as plt
x = [0 , 1, 2, 3]
y = [10, 100, 50, 80]
x2= [0, 1, 2, 3]
y2= [100, 70, 30, 30]

def new(val1,val2):
	z = []
	for i in range(4):
		z.insert(i, val1[i]/2 + val2[i])
	return z

#define a function which can perform z=x/2 + y. Then plot z.
#name your file as cal_and_plot.py

z = (new(x,y))
z2 = (new(x2,y2))

plt.bar(x, y, label = 'First Line')
plt.bar(x2, y2, label = 'Second Line')
plt.plot(x, z, label = 'Line z')
plt.plot(x, z2, label = 'Line z2')
plt.xlabel('Plot Number')
plt.ylabel('Sample Number')
plt.title('Sample Data\n 0-100')
plt.legend()
plt.show()
