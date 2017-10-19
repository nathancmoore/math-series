"""Test various functions of sum series."""


import pytest


@pytest.mark.parametrize('n', [0, "str", 4.6, [4, 5, 6], (1, 2, 3)])
def test_entry_validity(n):
    """Test for invalid entries."""
    from series import fibonacci, lucas, sum_series
    assert fibonacci(n) == 'Only integers above zero are valid!'
    assert lucas(n) == 'Only integers above zero are valid!'
    assert sum_series(n) == 'Only integers above zero are valid!'


@pytest.mark.parametrize('n, result', [(3, 1), (5, 3), (8, 13)])
def test_fibonacci(n, result):
    """Test for numbers in the Fibonacci Sequence."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', [(4, 4), (6, 11), (8, 29)])
def test_lucas(n, result):
    """Test for numbers in the Lucas Sequence."""
    from series import lucas
    assert lucas(n) == result


SUM_TABLE = [
    (5, 10, 16, 68),
    (6, 4, 2, 22),
    (8, 5, 7, 131)
]


@pytest.mark.parametrize('n, first_num, second_num, result', SUM_TABLE)
def test_sum_series(n, first_num, second_num, result):
    """Test for numbers in an arbitrary sum sequence."""
    from series import sum_series
    assert sum_series(n, first_num, second_num) == result
