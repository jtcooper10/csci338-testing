# CSCI 338 Testing Homework

In order to showcase thorough testing, we put together the world's most unpleasant command-line calculator! Type your math expression, with all arguments separated by spaces, in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

## TL;DR of Reverse Polish Notation

The expression is read from left to right, each number is placed on the stack, and each operation pulls 2 items off the stack, performs the operation, and puts the result onto the stack. The result of the expression is the final value on the stack.

For non-associative operations (like division), the arguments are considered left-to-right. For example, `6 3 /` is equivalent to `6 / 3` in regular math notation. Example: `2 4 * 3 -` means `(2 * 4) - 3`

The calculator has the following features:

## Allowed Math Operators

```sh
# 2 2 + means (2 + 2)
$ python3 mathexpr.py 2 2 +
Result (2 2 +): 4

# 7 1 - means (7 - 1)
$ python3 mathexpr.py 7 1 -
Result (7 1 -): 6

# 5 3 * means (3 * 5)
$ python3 mathexpr.py 5 3 *
Result (5 3 *): 15

# 2 8 / means (2 / 8)
$ python3 mathexpr.py 8 2 /
Result (2 8 /): 4

# 3 2 ^ means (3^2)
$ pyton3 mathexpr.py 3 2 ^
Result (3 2 ^): 9

# ++ Sums everything left in the list together
$ python3 mathexpr.py 1 2 3 4 5 ++
Result (1 2 3 4 5 ++): 15

# Chained together:
# 7 3 + 5 / 2 * = (7 + 3) / 5 * 2
$ python3 mathexpr.py 7 3 + 5 / 2 *
Result (7 3 + 5 / 2 *): 4
```
