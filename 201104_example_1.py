#get an initial guess 
guess_str = input("Guess a number: ") 
guess = int (guess_str)
number = 65
 
# while guess is range, keep asking 
while 0 <= guess <= 100:
	if guess > number:
		print ("Guessed Too High.")
		guess_str = input("Guess another number: ") 
		guess = int (guess_str)
	elif guess < number:
		print("Guessed Too Low.")
		guess_str = input("Guess another number: ") 
		guess = int (guess_str)
	elif guess > 100:
		print("Guess is not in range.")
		guess_str = input("Guess another number: ") 
		guess = int (guess_str)
	elif guess < 0:
		print("Guess is not in range.")
		guess_str = input("Guess another number: ") 
		guess = int (guess_str)
	elif guess == number:
		print("You guessed it. The number was:",number)
		guess_str = input("Guess another number: ") 
		guess = int (guess_str)
	else:
		print ("You quit early, the number was:",number) 
	
	
