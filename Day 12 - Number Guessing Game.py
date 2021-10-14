import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

# Select difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Select target
target = random.randint(1,100)

# Setting remaining guesses
guesses = 0
if difficulty == 'hard':
    guesses = 5
else:
    guesses = 10

# Ask user to make guess and print outcome
def make_guess(target):
    guess = int(input("Make a guess: "))
    if guess == target:
        print(f"You got it! The answer was {guess}.")
        exit()
    elif guess > target:
        print("Too high.")
    else:
        print("Too low. ")
    print("Guess again. ")
    return(guesses - 1)

# Request guess while remaining guesses > 0
while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number. ")
    guesses = make_guess(target)





