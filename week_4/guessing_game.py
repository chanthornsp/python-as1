# Create a program that simulates a guessing game:

secret_number = 8
guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if(guess > secret_number):
        print("Too high!")
    elif(guess < secret_number):
        print("Too low!")

print("You guessed it!")