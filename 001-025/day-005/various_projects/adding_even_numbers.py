# Program to add even numbers

target = int(input('Enter a number between 0 to 1000, to calculate its even sum: '))

# Variant 1 with modulo and condition
even_sum = 0
for i in range(1, target + 1):
    if i % 2 == 0:
        even_sum += i

print(f"The sum of all even is: {even_sum}")

# Variant 2 with step in range
even_sum = 0
for i in range(2, target + 1, 2):
    even_sum += i

print(f"The sum of all even is: {even_sum}")
