"""change me later."""


def fibonacci(n):
    """Generate Fibonacci numbers up to the nth one, and then returns it."""
    numbers = [0, 1]

    for i in range(n - 2):
        numbers.append((numbers[i]) + (numbers[i + 1]))

    return numbers[len(numbers - 1)]


def lucas(n):
    """Generate Lucas numbers up to the nth one, and then returns it."""
    numbers = [2, 1]

    for i in range(n - 2):
        numbers.append((numbers[i]) + (numbers[i + 1]))

    return numbers[len(numbers - 1)]
