a = input("give number:")
b,c = 1,0
while b <= int(a):
    c = c + b
    b = b + 1
print (a,b,c)
print ("Result: ", float(c)/b - 1)
