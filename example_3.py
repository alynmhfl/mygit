inches_str = input("How many icnhes of rain have fallen: ")
inches_int = int (inches_str)
volumn = (inches_int/12)*43560
gallons = volumn*7.48051945
print(inches_int,"in. rain on 1 acre is ", gallons, "gallons")