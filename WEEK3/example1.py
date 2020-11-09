#Adding a new example with break statement
#get an initial guess 

guess_str = input("Guess a number: ") 
guess = (guess_str)  
# while guess is range, keep asking 
while 0 <= guess <= 100: 
  if guess > number: 
     print ("Guessed Too High.") 
  elif guess < number: 
     print("Guessed Too Low.") 
  else: # correct guess, exit with break was: ",number) 
     print("You guessed it. The number is ",number)

  # keep going, get the next guess 
  guess_str = input("Guess a number: ") 
  if guess_str == 'none':
     break
  print ("You quitted early, the number was:",number) 
  
