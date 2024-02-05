# Average height of students in class program: Example: 156, 178, 165, 171, 187
# Here we'll take input in one string of student heights, storing them in variable and splitting each item to list
student_heights = input("Enter students height in one line separated by coma: ").split(", ")

# in this part we are converting each string item in list in to integer and replacing it in original list
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# here we will calculate average height of students
average = 0
for n in range(0, len(student_heights)):
    average += student_heights[n]

print(f"Total height of students is: {average}")
print(f"Number of students is {len(student_heights)}")
print(round(average / len(student_heights)))
