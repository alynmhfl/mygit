import matplotlib.pyplot as plt

def z_func (list_a, list_b):    //function to perform z=x/z+y
    z=[]
    for i in range(4):
        z.append(list_a[i]/2 + list_b[i])
    return z

x = [0, 1, 2, 3]
y = [10, 100, 50, 80]
x2 = [0, 1, 2, 3]
y2 = [100, 70, 30, 30]

z = z_func(x,y)
z2 = z_func(x2, y2)

plt.bar(x, y, label='First Line')                 #plot for y bars
plt.bar(x2, y2, label='Second Line')              #plot for x bars
plt.plot(x, z, color = 'green', label="z Line")   #plot for z line
plt.plot(x2, z2, color = 'red', label="z2 Line")  #plot for z2 line
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title ('Sample Date\n 0 - 100')
plt.legend()
plt.show()
