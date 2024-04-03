# Entry point for the simple calculator application.
# It orchestrates user interactions and calculations.

from calculation import perform_calculation
from user_choice import get_user_choice
from logo import logo

print(logo)

result = None
should_continue = True

while should_continue:
    # Use the previous result as the starting number if it exists
    if result is not None:
        print(f"Starting with result: {result}")
        num1 = result
    else:
        num1 = None

    # Perform a calculation. Note: perform_calculation should return None, False if the user wants to exit
    result, should_continue = perform_calculation(num1=num1)

    # Check if the user wants to continue after a successful operation
    if should_continue:
        user_choice = get_user_choice('Do you want to continue with another calculation? Yes or [Enter] for Yes, '
                                      'No for No: ', ["yes", "no"])
        if user_choice == "no":
            # Here's the change: Instead of setting should_continue to False, reset result and implicitly continue
            result = None
            print("Starting a new calculation...")
            # No need to change should_continue; it remains True, so the loop continues

print('Thanks for using my simple calculator software ^_^')
