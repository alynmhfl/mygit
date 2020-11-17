def celsius_to_fahrenheit(c_float):
  c_float = c*1.8 + 32
  return c_float

print("Conver celsius to fahrenheit")
c = float(input("enter celsius temp:"))
f_float = celsius_to_fahrenheit(c)
print(c, "C is ", f_float, "in fahrenheit")
