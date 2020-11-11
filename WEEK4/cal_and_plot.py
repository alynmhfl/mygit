import matplotlib.pyplot as plt
x = [0,1,2,3]
y = [10,100,50,80]
x2 = [0,1,2,3]
y2 = [100,70,30,30]

def newline(num1,num2):
  z = []
  for count in range(4):
    z.insert(count, num1[count]/2 + num2[count])
  return z

#define a function which can perform z = x/2 + y . then plot z.
z = (newline(x,y))
z2 = (newline(x2,y2))


plt.bar(x,y, label= 'first line', color='red')
plt.bar(x2,y2, label = 'second line', color='green')
plt.plot(x,z, label='z line', color='purple')
plt.plot(x,z2, label='z2 line', color='black')
plt.xlabel('plot number')
plt.ylabel('sample value')
plt.title ('sample data\n 0 - 100')
plt.legend()
plt.show()

