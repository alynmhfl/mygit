def celsius_to_fahrenheit(celsius_float):
    return celsius_float * 1.8 +32

#main
print("Convert celsius to fahrenheit")
celsius_float = float(input("Enter a Celsius temp : "))

fahrenheit_float = celsius_to_fahrenheit(celsius_float)

print(celsius_float,"Convert to ",fahrenheit_float,"Fahrenheit")
