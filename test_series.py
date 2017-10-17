import pytest


@pytest.mark.parametrize('n, result', [(3, 1), (5, 3), (8, 13)])
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', [(4, 4), (6, 11), (8, 29)])
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


SUM_TABLE = [
    (5, 10, 16, 68),
    (6, 4, 2, 22),
    (8, 5, 7, 131)
]


@pytest.mark.parametrize('n, first_num, second_num, result', SUM_TABLE)
def test_sum_series(n, first_num, second_num, result):
    from series import sum_series
    assert sum_series(n, first_num, second_num) == result
