# get an initial guess
guess = 22
str = int(input("Guess a number: "))
number = str
# while guess is range, keep asking
if number != guess:
    while str in range(0,100):
        if guess < str:
            print("Guessed Too High.")
            str = int(input("Guess a number: "))
        elif guess > str:
            print("Guessed Too Low.")
            str = int(input("Guess a number: "))
        else:  # correct guess, exit with break was: ",number)
            print("You guessed it. The number")
            break

# keep going, get the next guess

else:
    print("You quit early, the number was:", number)