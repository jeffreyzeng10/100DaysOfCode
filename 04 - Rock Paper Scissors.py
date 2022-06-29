#create a rock paper scissors game using randomization and lists
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

print(game_images[choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if(choice == computer_choice):
    print("Tie!")
elif(choice > 2 or choice < 0):
    print("You typed an invalid number. You Lose!")
elif(choice == 2 and computer_choice == 0):
    print("You Lose!")
elif(choice == 0 and computer_choice == 2):
    print("You Win!")
elif(choice > computer_choice):
    print("You Win!")
elif(computer_choice > choice):
    print("You Lose!")
exit()

