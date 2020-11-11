import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([10,100,50,80])
x2 = np.array([0,1,2,3])
y2 = np.array([100,70,30,30])

def equation(a,b):
	"""Equation of z = x/2 +y"""
	return a/2+b

z = equation(x,y)
z2 = equation(x2,y2)
plt.figure(1)
plt.bar(x,y, color="red",label="First Line")
plt.bar(x2,y2,color="orange", label="Second Line")
plt.plot(x,z, color="green",label="x,z plot")
plt.plot(x2,z2,color="purple" ,label="x2,z2 plot")
plt.xlabel("Plot Number")
plt.ylabel("Sample Value")
plt.title("Sample Data\n 0 - 100")
plt.legend()
plt.show()
