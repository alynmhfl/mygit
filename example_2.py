#calculate rainfall in gallons for some number of inches on 1 acre.
inches_str = input ("HOW MANY INCHES OF RAIN HAVE FALLEN:")
inches_int = float(inches_str)
volume = (inches_int/12) * 43560
gallons = volume * 7.48051945
print(inches_int," in. rain on 1 arce is", gallons, "gallons")
