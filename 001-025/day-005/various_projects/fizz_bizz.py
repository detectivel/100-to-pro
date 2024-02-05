# The FizzBuzz game
# Your program should print each number from 1 to target included
# When the number is divisible by 3 then instead if printing the number it should print "Fizz"
# When the number is divisible by 5 then instead if printing the number it should print "Buzz"
# And if the number is divisible by 3 and 5, 15 e.g. then instead if printing the number it should print "FizzBuzz"


target_number = int(input("Enter a last (from 1 to 100) number: "))
for number in range(1, target_number + 1):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
