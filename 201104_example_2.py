# initialize the input number and the sum 
number_str = input("Number: ")
the_sum = 0 

# Stop if a period (.) is entered. 
# remember, number str is a string until we convert it 
while number_str != "." :
	number = int(number_str) 
	if (number % 2) == 1: # number is not even (it is odd) 
		print ("Error, only even numbers please.") 
		number_str = input("Add number: ") 
	else:
		the_sum += number 
		number_str = input ( "Add number (input '.' to stop): ") 
print ("Thes sum is:", the_sum)
