#temperature conversion

def celsius_to_fahrenheit(celsius_float): #create function formula for fahrenheit conversion
	return celsius_float*1.8+32.0

#main prog.	
print(" Convert Celsius to Fahrenheit.")
celsius_float=float(input("enter a celsius temp: "))

#call the conversion formula
fahrenheit_float = celsius_to_fahrenheit(celsius_float)

#print the returned valua
print (celsius_float,"converts to ",fahrenheit_float," fahrenheit")
