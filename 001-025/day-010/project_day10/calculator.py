from math_operations import operations


def calculator(num1, num2, operator):
    """Calculate the result based on the operator and provided numbers."""
    operation_function = operations.get(operator)
    if operation_function:
        # Check if the operation is unary and only requires one argument
        if operator in ['sqrt']:  # Add any other unary operations to this list
            return operation_function(num1)
        else:
            return operation_function(num1, num2)
    else:
        return "Invalid operator. Please use '+', '-', '*', '/', '^', or 'sqrt'."
