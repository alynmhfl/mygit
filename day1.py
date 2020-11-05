import math
radius_str = input("ENTER THE RADIUS OF YOUR CIRCLE: ")
radius_int = int(radius_str)
circumference = 2*math.pi*radius_int
area = math.pi*(radius_int**2)
print ("THE CIRCUMFERENCE IS:", circumference, \
	"  AND THE AREA IS : ", area)

