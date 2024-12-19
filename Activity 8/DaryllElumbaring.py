import random
secret_number = random.randint(1, 20)
print("Welcome to 'Guess the Number' game!")
print("I'm thinking of a number between 1 and 20.")
guess = None

attempts = 0
while guess != secret_number:
    
    guess = int(input("Enter your guess: "))

    
    attempts += 1

    
    if guess < secret_number:
        print("Too low! Try guessing a higher number.")
    elif guess > secret_number:
        print("Too high! Try guessing a lower number.")
    else:
        print("Congratulations! You guessed the correct number!")
        
print(f"It took you {attempts} attempts to guess the correct number.")
print("Thank you for playing!")
