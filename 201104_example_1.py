#Program: Guess the number
#set a num to be guessed
number = 50

#get an initial guess 
guess_str = input("Guess a number from 0-100: ") 
guess = int(guess_str)  
 
# while guess is range, keep asking 
while 0 <= guess <= 100: 
  if guess > number: 
    print ("Guessed Too High.") 
  elif guess < number: 
    print("Guessed Too Low.") 
  else: # correct guess, exit with break was: ",number) 
    print("You guessed it. The number was: ", number)
    break 
  
  # keep going, get the next guess 
  guess_str = input("Please try again: ") 
  guess = int(guess_str) 
else: 
  print ("You quit early, the number was: ", number) 
