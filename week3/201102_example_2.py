percent = float(input("what is your %? : "))

if 90 <= percent < 100:
	print("you got an A! congratulations")
elif 80 <= percent < 90:
	print("you got an B! good job")
elif 70 <= percent < 80:
	print("you got an C! work harder")
elif 60 <= percent < 70:
	print("you got an D. please work harder next time")
else:
	print("oops! not good :(")
