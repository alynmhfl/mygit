def celcius(c_float):
	return c_float * 1.8 + 32

print("convert celcius to fahrenheit")
c_float = float(input("enter a temperature inn Celcius:"))

f_float = celcius(c_float)

print(c_float, "convert to ", f_float, "fahrenheit")
