#Conversion program
def celsius_to_fahrenheit(celsius_float):
	#""" Convert celsius to fahrenheit"""
	return celsius_float*1.8+32

#main part of the program
print("Convert celsius to fahrenheit")
celsius_float= float(input("Enter a Celsius temp: "))
#call the conversion function
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
#print the returned program 
print(celsius_float," convert to " , fahrenheit_float, " Fahrenheit")
