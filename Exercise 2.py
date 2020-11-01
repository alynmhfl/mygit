# Calculate rainfall in gallons for some number of inches on 1 acre.

inches_str = input("How many inches of rain has fallen: ")
inches_float = float(inches_str)
volume =(inches_float/12)*43560
gallons = volume*7.48051945

print(inches_float, "inches rain on 1 acre is", gallons, "gallons.")