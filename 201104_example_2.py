# initialize the input number and the sum 
number_str = input("Number: ")
the_sum = 0 

# Stop if a period (.) is entered. 
# remember, number str is a string until we convert it 
while number_str != ".":
	number = int(number_str) 
	while number % 2 == 1: # number is not even (it is odd) 
		print ("Error, only even numbers please.") 
		number_str = input("Number: ") 
		number = int(number_str)
	the_sum += number 
	print ("The sum is:", the_sum)
	number_str = input ( "Number: ") 
