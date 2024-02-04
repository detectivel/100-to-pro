# Rock, Scissors and Paper game.

import random

computer_choice = random.randint(1, 3)
print("Welcome to the Rock, Scissors and Paper game")
user_choice = int(input("Choose rock (1), paper (2), or scissors (3): \n"))
# Rock


rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

variations = [rock, paper, scissors]

if user_choice == 1 and computer_choice == 3:
    print(f"You choose {variations[user_choice - 1]}\n and computer choose {variations[computer_choice - 1]}\n")
    print("You win!")
elif computer_choice > user_choice:
    print(f"You choose {variations[user_choice - 1]}\n and computer choose {variations[computer_choice - 1]}\n")
    print("You lose!")
elif computer_choice == user_choice:
    print(f"You choose {variations[user_choice - 1]}\n and computer choose {variations[computer_choice - 1]}\n")
    print("Draw!")
else:
    print("Wrong input, you lose!")
