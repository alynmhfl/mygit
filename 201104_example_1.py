#get an initial guess 
guess_int = input("Guess a number (0 to 100 only): ") 
guess = int(guess_int)  
number = 50
# while guess is range, keep asking 
while 0 <= guess <= 100: 
	if guess > number: 
			print ("Guessed Too High.") 
	elif guess < number: 
		print ("Guessed Too Low. ")            
	else: # correct guess, exit with break was: ",number) 
		print("Yay! You guessed it. The number is", number,".")    
		break
		# keep going, get the next guess 
	guess_int = input("Guess a number (0 to 100 only): ") 
	guess = int(guess_int)  
else: 
	print ("You quit early, the number was:",number) 

