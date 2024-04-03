# Handles the core calculation logic, including user input, operation selection,
# and displaying the result.

from user_choice import get_user_choice
from math_operations import operations
from calculator import calculator
from display import format_display
from operation_validator import check_operation


def perform_calculation(num1=None):
    """Performs a single calculation using an optional starting number or operation choice.

    Args:
        num1 (float, optional): Starting number for the calculation. Defaults to None.

    Returns:
        tuple: A tuple containing the result (None if no calculation was performed) and
               a boolean indicating if the user wants to continue.
    """

    try:
        # Prompt for the first number if not provided
        if num1 is None:
            num1_input = input('What is your first number? ("no" for exit) ')
            if num1_input.lower() == "no":
                print('Exiting calculator.')
                return None, False
            num1 = float(num1_input)

        # Get the operation choice from the user
        valid_operations = list(operations.keys())
        operation_prompt = f'What operation? {valid_operations}: '
        operation = get_user_choice(operation_prompt, valid_operations + ["no"])

        if operation == "no":
            print('Exiting calculator.')
            return None, False

        num2 = None
        # For binary operations, prompt for the second number
        if operation != "sqrt":
            num2_input = input('What is your second number? ')
            num2 = float(num2_input)
            if operation == "/" and num2 == 0:
                print("Division by zero is not allowed. Please try a different operation or number.")
                return None, True  # Allows retrying

        # Perform the calculation
        result = calculator(num1, num2, operation) if operation != "sqrt" else calculator(num1, operation=operation)

        # Formatting and displaying the result
        print(f'{format_display(num1)} {operation} {format_display(num2) if num2 is not None else ""} = {format_display(result)}')

        return result, True

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        return None, True  # Allows retrying without exiting
    except ZeroDivisionError as e:
        print(e)
        return None, True  # Allows retrying without exiting

