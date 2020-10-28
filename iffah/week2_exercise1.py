#calculating rain fall in gallons

inches_str = input("how many inches of rain fallen: ")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume*7.48051945
print(inches_int, " inches rain on 1 acre is ", gallons, "gallons!" )