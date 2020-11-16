#Conversion Program

def celcius_to_fahrenheit(celcius_float):
    """Convert celcius to fahrenheit"""
    return celcius_float * 1.8 + 32

#main part of program
print("Convert Celcius to Fahrenheit")
celcius_float = float(input("Enter a celcius temp: "))
#Call the conversion function
fahrenheit_float = celcius_to_fahrenheit(celcius_float)
#print the return value
print(celcius_float,"Converts to ", fahrenheit_float," Fahrenheit")