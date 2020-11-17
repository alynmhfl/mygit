str_a = input("give a number:")
int_a = int(str_a)
b,c = 1,0
while b <= int_a:
    c = c + b
    b = b + 1
print (int_a,b,c)
print ("Result: ", float(c)/b-1)
