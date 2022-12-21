"""Написать тесты для ДЗ уроков 1-8  --  assertEqual """

from Task_1_2_Cod import my_func
from Task_1_2_Cod_2 import mult_namber
import math

def assert_equal_1():
    assert my_func(1, 2, 3) == 5, "Неверное решение домашнего задания"

def assert_equal_2():
    assert mult_namber == math.factorial(5), "Неверное считает факториал"


assert_equal_1()
