"""Написать тесты для ДЗ уроков 1-8"""

import unittest

import Task_2_cod_2

""" Импорт функции summ_1_3_5 из файла Task_2_cod"""
from Task_2_cod_2 import for_test
from Task_2_cod import summ_1_3_5, function_math
from Task_3_cod import division_2
from Seminar_3_Task_2_add import my_set_func


class TestHomeTask(unittest.TestCase):

    def test_summ_1_3_5(self):
        self.assertEqual(summ_1_3_5(), 9, ['Неверное решение'])

    def test_division_2(self):
        """Деление на ноль и правильность ввода"""
        self.assertRaises(Exception)
        division_2(2, 1)

    # division_2('e', 'd')

    def test_my_set_func(self):
        self.assertIn(3, my_set_func('3 5 7 7'), 'Error: Not Exist')

    def test_my_set_func_1(self):
        self.assertNotIn(4, my_set_func('3 5 7 7'), 'Error: Exist')

    def test_my_assertIsNotNone(self):
        self.assertIsNotNone(function_math(), "Error programm do not work!")

    def test_my_assertIsInstance(self):
        self.assertIsInstance(for_test(), Task_2_cod_2.Road, 'Error, '
                                                             'need class Road')


if __name__ == "__main__":
    unittest.main()
