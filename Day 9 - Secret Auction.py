#Secret Auction
#This program runs a price-sealed auction - an auction where nobody knows the other bids. 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os
clear = lambda: os.system('cls')

print(logo)
print("Welcome to the secret auction program. ")

auction_bids = {}
auction_finished = False
while auction_finished == False:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    more_bidders = input("Are there any other biddres? Type 'yes' or 'no'. ")
    auction_bids[name] = int(bid)
    if more_bidders == 'no':
        auction_finished = True
        clear()
    else:
        clear()

max_bid = 0
winner = ''
for name in auction_bids:
    bid = auction_bids[name]
    if bid > max_bid:
        max_bid = bid
        winner = name
print(f"The winner is {winner} with a bid of ${max_bid}.\n")
