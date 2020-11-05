# initialize the input number and the sum
 
number_str = input("Number: ")
number = int(number_str)
sum = 0 

# Stop if a period (.) is entered. 
# remember, number_str is a string until we convert it
 
while number_str != "." :
	# number is not even (it is odd) 
	if number % 2 == 1:
		print ("Error, only even numbers please.")
		number_str = input("Number: ")
		number = int(number_str)
		sum += number
	else:
		print ("Number is: ",number)
		number_str = input("Number: ")
		number = int(number_str)
		sum += number
	 
#number_str = input ( "Number: ") 
#print ("The sum is:")

#Reference
#num = int(input("Enter a number: "))
#if (num % 2) == 0:
#print("{0} is Even".format(num))
#else:
#print("{0} is Odd".format(num))
