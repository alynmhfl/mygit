import math

radius_str = input ('enter radius of circle:')
radius_int = int(radius_str)
circumference = 2*math.pi*radius_int
area = math.pi*(radius_int**2)

print ('circumference:', circumference, \
       'and area:', area)
