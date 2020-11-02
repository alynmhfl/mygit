percent_float = float(input("What is your percentage?"))

if 90 <= percent_float < 100:
    print("you recived an A")
elif 80 <= percent_float < 90:
    print("you received B")
elif 70 <= percent_float < 80:
    print("you received C")
elif 60 <= percent_float < 70:
    print("you received a D ")
else:
    print("Try again")