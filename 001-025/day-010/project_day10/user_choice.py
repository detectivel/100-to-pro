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