# Project 2 - Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_clients = int(input("How many people to split the bill? "))
total = round(bill / total_clients * ((tip_percent + 100)/100), 2)
print(f"Each person should pay ${total:.2f}")
