import matplotlib.pyplot as plt
x = [0,1,2,3,]
y = [10,100,50,80]
x2 = [0,1,2,3]
y2 = [100,70,30,30]

def function(x,y):
    z = []
    for i in range(4):
        z.insert(i,x[i]/2 + y[i])
    return z

z = function(x,y)
z2 = function(x2,y2)
plt.plot(x,z, label='z',color='red')
plt.plot(x2,z2, label='z2',color = 'black')

plt.bar(x,y,label = 'First Line')
plt.bar(x2,y2,label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data\n 0 - 100')
plt.legend()
plt.show()