from logo import logo
from math_operations import operations
print(logo)


def calculator(num1, num2, operator):
    operation_function = operations.get(operator)
    if operation_function:
        return operation_function(num1, num2)
    else:
        return "Invalid operator. Please use '+', '-', '*' or '/'."


def perform_calculation():
    try:
        num1_input = input('What is your first number? ')
        num1 = float(num1_input)

        valid_operations = ["+", "-", "*", "/"]
        operation_prompt = 'What operation? "+", "-", "*", "/": '
        operation = get_user_choice(operation_prompt, valid_operations + ["no"])

        if operation == "no":
            print('Exiting calculator.')
            return False  # User chose to exit

        num2_input = input('What is your second number? ')
        num2 = float(num2_input)

        if operation not in operations:
            print("Invalid operation. Please try again.")
            return False  # Indicates an invalid operation was attempted but keep the calculator running

        result = calculator(num1, num2, operation)
        if result == "Cannot divide by zero":
            print(result)
            return False

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        num1_display = int(num1) if num1.is_integer() else num1
        num2_display = int(num2) if num2.is_integer() else num2

        print(f'({num1_display} {operation} {num2_display} = {result})')
        return True  # Indicates successful calculation
    except ValueError:
        print("Invalid number input. Please enter numeric values.")
        return False  # Indicates failure due to invalid input


def get_user_choice(prompt, choices=None):
    """Asks the user for a choice until a valid answer is provided or allows exit."""
    while True:
        user_choice = input(prompt).lower()
        if user_choice == "" and choices is not None and "yes" in choices:
            return "yes"  # Treats empty input as "yes"
        elif choices is None or user_choice in choices:
            return user_choice
        else:
            if choices:
                print(f"Invalid response. Please answer with one of the following: {', '.join(choices)} or just press "
                      f"[Enter] for Yes.")
            else:
                print("Invalid response. Please enter a valid answer.")


should_continue = True
while should_continue:
    if perform_calculation():
        # After a successful calculation, ask if the user wants to continue.
        user_choice = get_user_choice('Do you want to continue? Yes or [Enter] for Yes, No for No: ', ["yes", "no"])
    else:
        # If the calculation wasn't successful, ask if they want to try again.
        user_choice = get_user_choice('Do you want to try again? Yes or No? ', ["yes", "no"])

    # Break the loop if user chooses "no", continue otherwise.
    if user_choice == "no":
        should_continue = False

print('Thanks for using my simple calculator software ^_^')
