# initialize the input number and the sum 
number_str = input("Number: ")
the_sum = 0 

# Stop if a period (.) is entered. 
# remember, number str is a string until we convert it 
while number_str != ".":
	number = int(number_str) 
	if number % 2 == 1: # number is not even (it is odd) 
		print ("Error, only even numbers please.") 
		break
	else:
		number_str = input("Number: ") 		
		the_sum = number + int (number_str)		
		print ("Thes sum is:", the_sum)
		the_sum=0
		
