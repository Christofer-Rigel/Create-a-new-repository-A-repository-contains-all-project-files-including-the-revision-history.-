import random as rd
scretnumber = rd.randint(1, 100)
print("Welcome to the guessing game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in ", scretnumber," attempts or less.")
for i in range(scretnumber):
    guess = int(input("Enter your guess: "))
    if guess < scretnumber:
        print("Your guess is too low.Attempts left =", scretnumber-i-1)
    elif guess > scretnumber:
        print("Your guess is too high.Attempts left =", scretnumber-i-1)
    elif guess == scretnumber:
        print("Congratulations! You guessed the number.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")