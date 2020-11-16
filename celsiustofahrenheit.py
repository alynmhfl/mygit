def celsius_to_fahrenheit(celsiusfloat):
    return celsiusfloat*1.8 + 32

print ('convert celsius to fahrenheit')
celsiusfloat=float(input('enter a celsius temp: '))
fahrenheitfloat=celsius_to_fahrenheit(celsiusfloat)
print((celsiusfloat),'celsius converts to', fahrenheitfloat,'fahrenheit')