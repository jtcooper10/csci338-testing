#!/usr/bin/env python3
import sys

def compute(ops: "list[str]"):
    stack = []
    for op in ops:
        if op.startswith("+"):
            if op == "++":
                stack = [sum(stack)]
            elif op == "+":
                stack.append(stack.pop() + stack.pop())
            else:
                # Assume it's a "positive value"
                stack.append(int(op[1:]))
        elif op == "-":
            opl, opr = stack.pop(), stack.pop()
            stack.append(opr - opl)
        elif op == "*":
            stack.append(stack.pop() * stack.pop())
        elif op == "/":
            opl, opr = stack.pop(), stack.pop()
            stack.append(opr // opl)
        elif op == "^":
            opl, opr = stack.pop(), stack.pop()
            stack.append(opr ** opl)
        else:
            # Assumed to be a value of some sort
            stack.append(int(op))

    if len(stack) > 1:
        raise ValueError("Too many values remaining")
    return stack.pop()

if __name__ == "__main__":
    args = []
    for arg in sys.argv[1:]:
        args.extend(arg.split(" "))
    print(f"Result ({' '.join(args)}): {compute(args)}")
