inches_str = input("How many inche of rain have fallen: ")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume * 7.48051945
print("{} in. rain on 1 acre is {} gallons".format(inches_int, gallons))
