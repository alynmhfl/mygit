import random  # get the random number module
number = random.randint(0,100) # get a random number
                               # between 0 and 100 inclusive
print("Hi-Lo Number Guessing Game: between 0 and 100 inclusive.")
print()

# get an initial guess
guess_str = input("Guess a number: ")
guess = int(guess_str)  # convert string to number

# while guess is range, keep asking
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed Too High.")
    elif guess < number:
        print("Guessed Too Low.")
    else:                # correct guess, exit with break
        print("You guessed it. The number was:",number)
        break
    # keep going, get the next guess
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early, the number was:",number)
