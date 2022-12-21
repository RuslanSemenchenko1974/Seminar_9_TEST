"""Написать тесты для ДЗ уроков 1-8"""

from Task_1_1_Cod import fibonacci, fibonacci_1


def assert_equal_1(x, y):
    x = fibonacci(x)
    assert x == y, "{} != {}".format(x, y)


def assert_equal_2(x, y):
    x = fibonacci_1(x)
    assert x == y, f"{x} != {y}"


assert_equal_1(2, 1)

assert_equal_2(-7, 13)
