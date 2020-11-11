import matplotlib.pyplot as plt

def getz(a,b):
    n=0
    z=[]
    while n<4:
        zvalue=a[n]/2 + b[n]
        z.append(zvalue)
        n+=1
    return z

x=[0,1,2,3]
y=[10,100,50,80]
x2=[0,1,2,3]
y2=[100,70,30,30]


plt.bar(x,y,label='first line')
plt.bar(x2,y2,color='red',label='second line')
z2=getz(x,y)
plt.bar (z2,y,color='yellow',label='z')
z3=getz(x2,y2)
plt.bar (z3,y2,color='green',label='z2')
plt.xlabel('plot number')
plt.ylabel('sample value')
plt.title('sample data\n 0-100')
plt.legend()
plt.show()
