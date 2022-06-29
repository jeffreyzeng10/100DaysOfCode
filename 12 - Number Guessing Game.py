import random

EASY_GAME_GUESSES = 10
HARD_GAME_GUESSES = 5

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    # Select difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Select target
    target = random.randint(1,100)

    # Setting remaining guesses
    if difficulty == 'hard':
        guesses = HARD_GAME_GUESSES
    else:
        guesses = EASY_GAME_GUESSES

    # Request guess while remaining guesses > 0
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number. ")
        make_guess(target)
        print("Guess again. ")
        guesses -= 1


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
    return

start_game()



