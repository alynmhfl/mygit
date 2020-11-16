def celsius_to_fahrenheit(celsius_float):
	"""Convert Celsius to Fahrenheit"""
	return celsius_float*1.8 + 32

print("Conver Celsius to Fahrenheit.")
celsius_float = float(input("Enter a Celsius temperateure: "))
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
print(celsius_float,"converts to Fahrenheit is ",fahrenheit_float,".")