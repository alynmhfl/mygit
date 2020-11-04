#get an initial guess
number_str = input("Number to be guess: ")
number = int(number_str)

guess_str = input("Guess a number: ")
guess = int(guess_str)
# while guess is range, keep asking
while 0 <= guess <= 100:

    if guess > number:
        print ("Guessed Too High.")
    elif guess < number:
        print("Guessed Too Low.")
    else: # correct guess, exit with break was: ",number)
        print("You guessed it. The number is {}".format(guess))
    # keep going, get the next guess
    guess_str = input("Guess a number: ")
    if guess_str == 'q':
        break
    guess = int(guess_str)

print ("You quit early, the number was:",number)
