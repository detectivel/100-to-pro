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
    """Returns the division of n1 by n2."""
    return n1 / n2


def sqrt(n1):
    """Returns the square root of n1."""
    return n1 ** 0.5


def power(n1, n2):
    """Returns n1 raised to the power of n2."""
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "sqrt": sqrt,  # Note: This operation only needs one number
}
