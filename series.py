"""Definitions of functions to return the nth value of various series."""


def fibonacci(n):
    """Generate Fibonacci numbers, then return the nth one."""
    numbers = [0, 1]

    for i in range(n - 2):
        numbers.append((numbers[i]) + (numbers[i + 1]))

    return numbers[len(numbers) - 1]


def lucas(n):
    """Generate Lucas numbers, then return the nth one."""
    numbers = [2, 1]

    for i in range(n - 2):
        numbers.append((numbers[i]) + (numbers[i + 1]))

    return numbers[len(numbers) - 1]


def sum_series(n, first_num=0, second_num=1):
    """Generate an arbitrary sum series, then return the nth value."""
    numbers = [first_num, second_num]

    for i in range(n - 2):
        numbers.append((numbers[i]) + (numbers[i + 1]))

    return numbers[len(numbers) - 1]


if __name__ == "__main__":
    print(__doc__)
    print("fibonacci(): " + fibonacci.__doc__)
    print("lucas(): " + lucas.__doc__)
    print("sum_series(): " + sum_series.__doc__)
