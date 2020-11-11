import matplotlib.pyplot as plt

x = [0,1,2,3]
y = [10,100,50,80]
x2 = [0,1,2,3]
y2 = [100,70,30,30]
length = len(x)

#define a function which can perform z = x/2 + y. Then plot z
def z_value(x,y):
    z = [0]*4
    for i in range(length):
        z[i] = x[i]/2 + y[i]
        print(z[i])
    return z

z1 = z_value(x,y)
z2 = z_value(x2,y2)


plt.plot(x,z1,color = 'black',label = 'z1 line')
plt.plot(x2,z2,color = 'green',label = 'z2 line')
plt.bar(x,y,color = 'yellow',label = 'First Line')
plt.bar(x2,y2,label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data\n 0-100')
plt.legend()
plt.show()
