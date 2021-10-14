#TODO: Add functionality for ace - convert 11 to 1

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
clear = lambda: os.system('cls')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def start_game():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        clear()
        print(logo)
        player_cards = random.choices(cards, k=2)
        computer_cards = random.choices(cards, k=2)
        show_score(player_cards, computer_cards)

        # Ask if player wants another card
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        while hit == 'y':
            player_cards.append(random.choice(cards))
            show_score(player_cards, computer_cards)
            if sum(player_cards) == 21:
                show_final(player_cards, computer_cards)
                print("21! You Win")
                return start_game()
            # Going bust
            elif sum(player_cards) > 21:
                if 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1
                    show_score(player_cards, computer_cards)    
                else:
                    show_final(player_cards, computer_cards)
                    print("You went over. You Lose")
                    return start_game()
            else:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
        
        while sum(computer_cards) <= 16:
            computer_cards.append(random.choice(cards))
            if sum(computer_cards) == 21:
                show_final(player_cards, computer_cards)
                print("Computer hit 21. You Lose")
            if sum(computer_cards) > 21:
                if 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1
                    show_score(player_cards, computer_cards)    
                else:
                    show_final(player_cards, computer_cards)
                    print("You Win")
                    return start_game()
        show_final(player_cards, computer_cards)
        if sum(player_cards) > sum(computer_cards):
            print("You Win")
        else:
            print("You Lose")
        start_game()
    else:
        return

def show_score(player_cards, computer_cards):
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def show_final(player, computer):
    print(f"Your final hand: {player}, final score: {sum(player)}")
    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")

start_game()