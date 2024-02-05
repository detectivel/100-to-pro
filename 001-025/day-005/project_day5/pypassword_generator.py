# The password generator project
# Use only lists, random, loops and strings manipulations

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '_', '`', '~']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Variant 1
pass_list = []
for i in range(0, nr_letters):
    pass_list.append(random.choice(letters))

pass_numbers = []
for i in range(0, nr_numbers):
    pass_list += random.choice(numbers)

pass_symbols = []
for i in range(0, nr_symbols):
    pass_list.insert(i, random.choice(symbols))

# Shuffle the list of characters randomly
random.shuffle(pass_list)

# Join the list back into a string
randomized_string = ''.join(pass_list)
print(f"Your password is: \033[1m{randomized_string}\033[0m and it's length is: {len(randomized_string)}")

# Variant 2
# Generate password list using list comprehensions
pass_list = [random.choice(letters) for _ in range(nr_letters)] + \
            [random.choice(symbols) for _ in range(nr_symbols)] + \
            [random.choice(numbers) for _ in range(nr_numbers)]

# Shuffle the list of characters randomly
random.shuffle(pass_list)

# Join the list back into a string
randomized_string = ''.join(pass_list)
print(f"Your password is: \033[1m{randomized_string}\033[0m and it's length is: {len(randomized_string)}")
