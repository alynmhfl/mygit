
#Convert celsius to fahrenheit
def cel_to_fahrenheit(cel_float):
    return cel_float *1.8 +32

print ("Covert Celcius to Fahrenheit")
celsius_float_input = float(input("Enter your temp in cel: "))
fah_float =  cel_to_fahrenheit(celsius_float_input)
print("{} convert to {}".format(celsius_float_input,fah_float))