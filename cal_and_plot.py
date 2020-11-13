import matplotlib.pyplot as plt
x = [ 0, 1, 2, 3 ]
y = [ 10, 100, 50, 80 ]
x2 = [ 0, 1, 2, 3 ]
y2 = [ 100, 70, 30, 30 ]
z=[]
z2=[]
#define a function which can perform z = x/2 +y. then plot z.
for x_int in x:
	for y_int in y:
		zvalue=int(x_int)/2+int(y_int)
		z.append(zvalue)	
for x2_int in x2:
	for y2_int in y2:
		z2value =int(x2_int)/2+int(y_int)
		z2.append(z2value)
# name your file as cal_and_plot.py


plt.bar(x, y,color='green', label = 'first line')
plt.bar(x2,y2,color='blue', label = 'second line')
plt.bar(z,z2, label = 'third line')
plt.xlabel( 'Plot Number')
plt.ylabel( 'Sample Value')
plt.title( 'Sample Data\n 0 - 100')
plt.legend()
plt.show()
