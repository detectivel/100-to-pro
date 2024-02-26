from math_operations import operations


def calculator(num1, num2, operator):
    operation_function = operations.get(operator)
    if operation_function:
        return operation_function(num1, num2)
    else:
        return "Invalid operator. Please use '+', '-', '*' or '/'."
