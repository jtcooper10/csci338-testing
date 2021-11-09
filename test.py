#!/usr/bin/env python3
import unittest
import mathexpr


class TestMathExpressions(unittest.TestCase):
    def test_that_values_work(self):
        result = mathexpr.compute(["101"])
        self.assertEqual(result, 101, f"Computation was incorrect (got {result}, expected 101)")

    def test_that_explicit_positive_numbers_work(self):
        result = mathexpr.compute(["+12"])
        self.assertEqual(result, 12, f"Computation was incorrect (got {result}, expected 22)")

    def test_that_explicit_negative_numbers_work(self):
        result = mathexpr.compute(["-19"])
        self.assertEqual(result, -19, f"Computation was incorrect (got {result}, expected 54)")

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

    def test_that_summations_work(self):
        result = mathexpr.compute(["1", "2", "4", "3", "7", "++"])
        self.assertEqual(result, 17, f"Computation was incorrect (got {result}, expected 17)")

    def test_that_exponents_work(self):
        result = mathexpr.compute(["2", "8", "^"])
        self.assertEqual(result, 256, f"Computation was incorrect (got {result}, expected 256)")

    def test_decimal_raises_error(self):
        for val in ["3.1", "+3.1", "-3.1"]:
            with self.subTest("decimal error", value=val):
                with self.assertRaises(mathexpr.BadOperandError):
                    mathexpr.compute([val])

    def test_no_input_raises_error(self):
        with self.assertRaises(IndexError):
            mathexpr.compute([])

    def test_too_many_operators_raises_error(self):
        for op in ["+", "-", "*", "/", "^"]:
            with self.subTest("operand count error", operator=op):
                with self.assertRaises(mathexpr.TooFewOperandsError):
                    mathexpr.compute(["2", "3", "*", op])

    def test_too_many_numbers_raises_error(self):
        with self.assertRaises(mathexpr.TooManyOperandsError):
            mathexpr.compute(["5", "2", "3", "*"])

    def test_wrong_order_raises_error(self):
        with self.assertRaises(mathexpr.TooFewOperandsError):
            mathexpr.compute(["+", "5", "2"])

if __name__ == "__main__":
    unittest.main(TestMathExpressions())
