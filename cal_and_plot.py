import matplotlib.pyplot as plt

x=[ 0, 1, 2, 3]
y=[ 10, 100, 50, 80]
x2=[ 0, 1, 2, 3]
y2=[ 100, 70, 30, 30]
lx=len(x)

#define a function which can perform z= x/2+y. Then plot z.
#Name your file as cal_and_plot.py

def cal (x,y):
	z=[0]*4
	for i in range(lx):
		z[i]=x[i]/2+y[i]
		print(z[i])
	return z

z1=cal(x,y)
z2=cal(x2,y2)

plt.plot(x,z1,label='z1 Line',color='black')
plt.plot(x,z2,label='z2 Line',color='blue')
plt.bar(x,y,label= 'First Line')
plt.bar(x2,y2,label= 'Second Line')
plt.xlabel('PLot Number')
plt.ylabel('Sample Value')
plt.title('Sample Data\n 0-100')
plt.legend()
plt.show()
