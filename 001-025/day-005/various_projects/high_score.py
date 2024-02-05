# Program that calculates the highest score from a List of scores:
# Limitation: yuo cannot use max or min functions

students_score = [78, 65, 89, 86, 55, 91, 64, 89] # it can be also done with input, split and for loop for ints
highest_score = 0

for score in students_score:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
