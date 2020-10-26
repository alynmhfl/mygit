import math

radius_str = input("enter radius of circle = ")
radius_int = input(radius_str)

circumference = 2*math.pi*(radius_int)
area = math.pi*(radius_int)**2

print("the circumference is:", circumference, \
	"and the area is: ", area)