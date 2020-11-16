#Coversion program

def cel_to_fahren(x_float,x1_float):
    z= x_float * 1.8 + 32
    z1= x1_float *1.8 + 32
    return z,z1

#main part of the program
print("Convert Celsuis to Fahrenheit.")

x_float= float(input("Enter a Celsius temp: "))
x1_float= float(input("Enter another Celsius temp: "))

#call the conversion function
fahrenheit_float= cel_to_fahren(x_float,x1_float)

#print the returned value
print(x_float,x1_float, "converts to", fahrenheit_float, "Fahrenheit")
