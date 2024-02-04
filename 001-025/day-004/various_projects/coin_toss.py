# Coin Toss game
import random

print("Welcome to Coin Toss game!")
print("Throwing a coin. And the result is ...")
coin = random.randint(0,1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
