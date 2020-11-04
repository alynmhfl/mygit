# get an initial guess
guess_str = input("Guess a number: ")
guess = int(guess_str)
number = 17
 
# while guess is range, keep asking 
while 0 <= guess <= 100:
    if guess > number:
        print ("Guessed Too High.")
        guess_str = input("Guess a number: ")
        guess = int(guess_str)
    elif guess < number:
        print("Guessed Too Low.")
        guess_str = input("Guess a number: ")
        guess = int(guess_str)
    else:
        print("You guessed it. The number was: " ,number)
        guess_str = input("Guess a number: ")
        guess = int(guess_str)

print ("You quit early, the number was: " ,number)
guess_str = input("Guess a number: ")
guess = int(guess_str)
