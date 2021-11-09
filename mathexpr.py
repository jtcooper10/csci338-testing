#!/usr/bin/env python3
import sys

class TooFewOperandsError(Exception):
    def __init__(self, message: "str" = None, operator: "str" = None):
        if message is None:
            message = "Not enough operands for operator"

        super().__init__(message)
        self.operator = operator

class TooManyOperandsError(Exception):
    def __init__(self, message: "str" = None, num_operands: "list[int]" = None):
        if num_operands is None:
            num_operands = []
        if message is None:
            message = "Too many operands remaining"

        super().__init__(message)
        self.num_operands = num_operands

class BadOperandError(ValueError):
    def __init__(self, message: "str" = None, operand: "str" = None):
        if operand is None:
            operand = "None"
        if message is None:
            message = "Could not convert operand to integer"

        super().__init__(message)
        self.operand = operand

def compute(ops: "list[str]"):
    stack = []
    for op in ops:
        try:
            if op.startswith("+"):
                if op == "++":
                    stack = [sum(stack)]
                elif op == "+":
                    try:
                        stack.append(stack.pop() + stack.pop())
                    except IndexError:
                        raise TooFewOperandsError(operator="+")
                else:
                    # Assume it's a "positive value"
                    stack.append(int(op[1:]))
            elif op == "-":
                try:
                    opl, opr = stack.pop(), stack.pop()
                except IndexError:
                    raise TooFewOperandsError(operator="-")
                stack.append(opr - opl)
            elif op == "*":
                try:
                    stack.append(stack.pop() * stack.pop())
                except IndexError:
                    raise TooFewOperandsError(operator="*")
            elif op == "/":
                try:
                    opl, opr = stack.pop(), stack.pop()
                except IndexError:
                    raise TooFewOperandsError(operator="/")
                stack.append(opr // opl)
            elif op == "^":
                try:
                    opl, opr = stack.pop(), stack.pop()
                except IndexError:
                    raise TooFewOperandsError(operator="^")
                stack.append(opr ** opl)
            else:
                # Assumed to be a value of some sort
                stack.append(int(op))
        except ValueError:
            raise BadOperandError(operand=op)

    if len(stack) > 1:
        raise TooManyOperandsError(num_operands=len(stack))
    return stack.pop()

def main(argv) -> "int":
    try:
        result = compute(argv)
        print(f"Result ({' '.join(argv)}): {result}")
        return 0
    except:
        # Nested try-catch, to reduce duplicate code
        # All exceptions are handled in the same way: print, then return 1
        try:
            raise
        except ZeroDivisionError:
            print(" ! Attempted to divide by zero")
        except TooFewOperandsError as err:
            print(f" ! Not enough operands on stack for operator {err.operator}")
        except TooManyOperandsError as err:
            print(f" ! Ambiguous result; {err.num_operands-1} too many operands")
        except BadOperandError as err:
            print(f" ! Not a valid integer or operator: {err.operand}")
        finally:
            return 1

if __name__ == "__main__":
    args = []
    for arg in sys.argv[1:]:
        args.extend(arg.split(" "))

    exit(main(args))
