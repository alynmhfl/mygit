# Conversion Program 

def celsius_to_fahrenheit(celsius_float):
	'''Convert Celsius to Fahrenheit'''
	return celsius_float * 1.8 + 32
	
# Main part of the program 
print("Convert Celsius to Fahrenheit.")
celsius_float = float(input("Enter a Celsius temp: "))

# Call the conversion function 
fahrenheit_float = celsius_to_fahrenheit(celsius_float)

# Print the returned value 
print(celsius_float, " converts to ",fahrenheit_float, "Fahrenheit.")
