def celsius_to_fahrenheit(c_float):
	#Convert Celsius to Fahrenheit
	return c_float*1.8 + 32

c_float = float(input("Enter Celsius -> "))
f_float = celsius_to_fahrenheit(c_float)
print(c_float,"Fahrenheit ->",f_float,".")