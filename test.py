#!/usr/bin/env python3
import unittest
import mathexpr


class TestMathExpressions(unittest.TestCase):
    def test_that_plus_signs_work(self):
        result = mathexpr.compute(["2", "5", "+"])
        self.assertTrue(result == 7)

    def test_that_minus_signs_work(self):
        result = mathexpr.compute(["10", "5", "-"])
        self.assertTrue(result == 5)

    def test_that_division_signs_work(self):
        result = mathexpr.compute(["8", "4", "/"])
        self.assertTrue(result == 2)

    def test_that_multiplication_signs_work(self):
        result = mathexpr.compute(["2", "3", "*"])
        self.assertTrue(result == 6)

    def test_decimal_raises_error(self):
        with self.assertRaises(Exception):
            mathexpr.compute(["2", "3.1", "*"])

    def test_no_input_raises_error(self):
        with self.assertRaises(IndexError):
            mathexpr.compute([])

    def test_too_many_operands_raises_error(self):
        with self.assertRaises(IndexError):
            result = mathexpr.compute(["2", "3", "*", "/"])

    def test_too_many_numbers_raises_error(self):
        with self.assertRaises(ValueError):
            result = mathexpr.compute(["5", "2", "3", "*"])

    def test_wrong_order_raises_error(self):
        with self.assertRaises(IndexError):
            result = mathexpr.compute(["+", "5", "2"])

if __name__ == "__main__":
    unittest.main(TestMathExpressions())
