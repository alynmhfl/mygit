import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]

def function(a,b):
	z = []
	for count in range(4):
		z.insert(count, a[count]/2 + b[count])
	return z

z =  function(x,y)
z2 = function(x2,y2)

plt.bar(x,y, label= 'first line')
plt.bar(x2,y2, label = 'second line')
plt.plot(x,z, label='z', color = 'red')
plt.plot(x,z2, label='z2', color = 'black')
plt.xlabel('plot number')
plt.ylabel('sample value')
plt.title ('sample data\n 0 - 100')
plt.legend()
plt.show()

