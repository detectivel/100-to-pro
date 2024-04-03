def format_display(number):
    """Formats the number for display: as an integer if whole, or as a float otherwise.

    Args:
        number (float): The number to format.

    Returns:
        Union[int, float]: The number formatted as an int if it's a whole number, or as a float otherwise.
    """
    # Ensure number is treated as float for consistency
    number = float(number)
    # If the number is a whole number, return it as an int; otherwise, return as a float
    return int(number) if number.is_integer() else number
