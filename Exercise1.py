#Calculate rainfall with int
inches_str = input("How many inches of rain have fallen: ")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume * 7.48051945
print(inches_int, " in. rain on 1 acre is", gallons, " gallons")

#Calculate rainfall with float
inches_str = input("How many inches of rain have fallen: ")
inches_int = float(inches_str)
volume = (inches_int/12)*43560
gallons = volume * 7.48051945
print(inches_int, " in. rain on 1 acre is", gallons, " gallons")
