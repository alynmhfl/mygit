import matplotlib.pyplot as plt
x = [ 0, 1, 2, 3 ]
y = [ 10, 100, 50, 80 ]
x2 = [ 0, 1, 2, 3 ]
y2 = [ 100, 70, 30, 30 ]

#define a function which can perform z = x/2 + y. Then plot z.
#Name your file as cal_and_plot.py

plt.bar(x,y,label = 'First line')
plt.bar(x2,y2, label = 'Second line')
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title( 'Sample Data\n 0 -100')
plt.legend()
plt.show()
