def add(n1, n2):
    """Returns the sum of n1 and n2."""
    return n1 + n2


def subtract(n1, n2):
    """Returns the difference of n1 and n2."""
    return n1 - n2


def multiply(n1, n2):
    """Returns the product of n1 and n2."""
    return n1 * n2


def divide(n1, n2):
    """Returns the division of n1 by n2. Raises ZeroDivisionError for n2 = 0."""
    try:
        return n1 / n2
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
