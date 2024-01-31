# Welcome to the simple variation of Treasure Island game
# with if/elif/else statements

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if cross_road == "left":
    action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
                   "Type 'swim' to swim across\n")
    if action == "wait":
        door = input("You take the boat and get to the Island. You meet there three doors, 'blue', 'red' and 'yellow'. "
                     "Which one will you choose? \n")
        if door == "yellow":
            print("Congratulations! You won.")
        elif door == "blue":
            print("You have been eaten by beasts. Game over")
        elif door == "red":
            print("You've been burned by fire. Game over")
        else:
            print("Game over")
    else:
        print("You've been attacked by trout. Game over.")
else:
    print("You felt in to the Hole. Game over.")
