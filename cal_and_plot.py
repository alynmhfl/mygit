import matplotlib.pyplot as plt

x   = [0,1,2,3]
y   = [10,100,50,80]
x2  = [0,1,2,3]
y2  = [100,70,30,30]
def func_plot (first_val, second_val):
    z= []
    for count in range(4):
        z.insert(count, first_val[count]/ 2 + second_val[count] )
    return z

z =  (func_plot(x,y))
z2 =  (func_plot(x2,y2))

plt.bar(x,y,label='First Line')
plt.bar(x2,y2,label='Second Line')
plt.plot(x, z,'k-',label='First z')
plt.plot(x2, z2,'g-',label='second z')
plt.xlabel('Plot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data \n 0-100')
plt.legend()
plt.show()
