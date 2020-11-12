
import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]
x3 = [0, 1, 2, 3]
z = []

for i in range(len(x)):
    z.append(x[i]/2 + y[i])

print(z)

plt.bar(x, y, label= 'First Line' )
plt.bar(x2, y2, label= 'Second line' )
plt.bar(x3, z, label= 'Third line')
plt.xlabel('Plot number')
plt.ylabel('sample value')
plt.title('Sample Data \n 0 -100')
plt.legend()
plt.show()
