"""Definitions of functions to return the nth value of various series."""


def fibonacci(n):
    """Generate Fibonacci numbers, then return the nth one."""
    if n < 1 or type(n) is not int:
        return 'Only integers above zero are valid!'

    numbers = [0, 1]

    for i in range(n - 2):
        numbers.append(numbers[i] + numbers[i + 1])

    return numbers[n - 1]


def lucas(n):
    """Generate Lucas numbers, then return the nth one."""
    if n < 1 or type(n) is not int:
        return 'Only integers above zero are valid!'

    numbers = [2, 1]

    for i in range(n - 2):
        numbers.append(numbers[i] + numbers[i + 1])

    return numbers[n - 1]


def sum_series(n, first_num=0, second_num=1):
    """Generate an arbitrary sum series, then return the nth value."""
    if n < 1 or type(n) is not int:
        return 'Only integers above zero are valid!'

    numbers = [first_num, second_num]

    for i in range(n - 2):
        numbers.append(numbers[i] + numbers[i + 1])

    return numbers[n - 1]


if __name__ == "__main__":
    output = """
    This module contains three functions.

    fibonacci(n):
        Returns the nth number in the Fibonacci Sequence.

    >>>fibonacci(2)
    {}

    lucas(n):
        Returns the nth number in the Lucas Sequence.

    >>>lucas(3)
    {}

    sum_series(n):
        Returns the nth number in an arbitrary sum sequence.

    >>>sum_series(1, 5, 4)
    {}
"""
    print(output.format(fibonacci(2), lucas(3), sum_series(1, 5, 4)))
