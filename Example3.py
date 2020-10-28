inches_str = input("How many inches of rain have fallen: ")
inches_float = int(inches_str)
volume = (inches_float/12)*43560
gallons = volume * 7.48051945
print (inches_float, " in. rain one 1 acre is ", gallons, " gallons")
