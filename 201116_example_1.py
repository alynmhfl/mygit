# Conversion program

def celsius_to_farenheit(celsius_float) :
# """ Convert Celsius to Fahrenheit. """
  return celsius_float * 1.8 + 32.0

# Main part of the program
celsius_float = float(input("Enter a Celsius temp: "))

# Call the conversion function
fahrenheit_float = celsius_to_fahrenheit(celsius_float)

# Print the returned value
print(celsius_float," converters to ",fahrenheit_float," Farenheit")

