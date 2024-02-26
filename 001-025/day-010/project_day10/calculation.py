from user_choice import get_user_choice
from math_operations import operations
from calculator import calculator


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

        if operation == "/" and num2 == 0:
            print("Cannot divide by zero. Restarting calculator")
            perform_calculation()

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
