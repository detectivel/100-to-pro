from calculation import perform_calculation
from user_choice import get_user_choice
from logo import logo


print(logo)

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
