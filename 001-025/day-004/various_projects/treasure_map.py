# Treasure map game
import random

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
treasure_map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
print("""Example of choosing the spot B2
   A    B    C
1 " "  " "  " "
2 " "  "X"  " "
3 " "  " "  " "
""")
position = input("Enter your position (A1, A2 ,A3, B1, B2, B3, C1, C2, C3: ")
position_index = int(position[1]) - 1
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

if position_index == 0:
    treasure_map[position_index][letter_index] = "X"
elif position_index == 1:
    treasure_map[position_index][letter_index] = "X"
elif position_index == 2:
    treasure_map[position_index][letter_index] = "X"
else:
    print("Invalid position")

print(f" {treasure_map[0]}\n {treasure_map[1]}\n {treasure_map[2]}\n")
