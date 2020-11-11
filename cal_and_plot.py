import matplotlib.pyplot as plt
x = [0,1,2,3]
y = [10,100,50,80]
x2 = [0,1,2,3]
y2 = [100,70,30,30]

def cal_z(x,y):
    z = [x/2 + y for (x, y) in zip(x, y)]
    return z

plt.bar(x,y, color='b', width=0.1,label= 'First Line')
plt.bar([i+0.1 for i in x2],y2,color='r', width=0.1, label='Second Line')
plt.bar([i+0.2 for i in x],cal_z(x,y), color='g', width=0.1,label= 'z1 Line')
plt.bar([i+0.3 for i in x],cal_z(x2,y2),color='y', width=0.1, label='z2 Line')

plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data\n 0 - 100')
plt.legend(loc=2)

plt.xticks([i+0.15 for i in x],x)
plt.show()
