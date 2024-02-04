# Banker roulette game
# Condition: Cannot use choice() function
# Use this names for example: Jack, John, Amy, Bryan, Bob, Jennifer
import random

print("Welcome to the Banker Roulette Program!")

user_input = input("Enter names of people who went to bar: ")
names = user_input.split(", ")

person_who_will_pay = random.randint(0, len(names) - 1)
print(f"And the one who will pay the total bill is: {names[person_who_will_pay]}")
