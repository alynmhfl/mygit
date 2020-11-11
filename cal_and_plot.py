import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
z = []
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]
z2= []

def z_calculations(X, Y):
	Z=(X/2)+Y
	return Z

for k in range(4):
	z.append(z_calculations(x[k], y[k]))
	z2.append(z_calculations(x2[k], y2[k]))

fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection = '3d')

ax.plot(x,y,z,'r')
ax.plot(x2,y2,z2,'b')

ax.set_xlim3d(0, 4)
ax.set_ylim3d(105, 0)
ax.set_zlim3d(0, 105)

ax.set_xlabel('Plot Number')
ax.set_ylabel('Sample Value')
ax.set_zlabel('Result')

plt.title('Sample Data\n 0 - 100')
plt.legend()
plt.show()
