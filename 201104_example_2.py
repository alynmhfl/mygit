#Program: Summation of even numbers
# initialize the input number and the sum 
number_str = input("Please enter the number: ")
sum_num = 0 

# Stop if a period (.) is entered. 
# remember, number_str is a string until we convert it 
while number_str != ".":
  number = int(number_str)
  if number % 2 == 1: # number is not even (it is odd) 
    print ("Error, only even numbers please.") 
    number_str = input("Please enter the number again: ")
    continue  
  sum_num += number 
  number_str = input ( "Please enter another number('.' if you want to exit): ") 

print ("Thes sum is: ", sum_num)
