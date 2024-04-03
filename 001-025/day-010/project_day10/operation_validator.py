from math_operations import operations


def check_operation(operator):
    """Check if the math operation is in the pool of valid operations."""
    return operator in operations
