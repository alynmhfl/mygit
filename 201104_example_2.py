# initialize the input number and the sum

str = input("Number: ")
sum = 0

# Stop if a period (.) is entered.
# remember, number str is a string until we convert it
while str != ".":
    number = int(str)
    if number % 2 == 1:  # number is not even (it is odd)
        print("Error, only even numbers please.")
        str = input("Number: ")
        continue
    sum += number
    str = input("Number: ")
print("Thes sum is: ",sum)


