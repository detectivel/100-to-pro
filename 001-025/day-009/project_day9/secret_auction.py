from replit import clear
from logo import logo
from highest_bidder import find_highest_bidder

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type "yes" or "no". ')
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()

the_winner = find_highest_bidder(bids)
print(f'The winner is {the_winner} and it was {bids[the_winner]}')
