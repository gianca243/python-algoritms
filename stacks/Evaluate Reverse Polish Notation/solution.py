import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                add = stack.pop()
                stack[-1] += add
            elif item == "-":
                minus = stack.pop()
                stack[-1] -= minus
            elif item == "/":
                div = stack.pop()
                if div == 0:
                    stack[-1] *= 0
                else:
                    stack[-1] /= div
                    if stack[-1] < 0:
                        stack[-1] = math.ceil(stack[-1])
                    else:
                        stack[-1] = math.floor(stack[-1])
            elif item == "*":
                times = stack.pop()
                stack[-1] *= times
            else:
                stack.append(int(item))
        return stack[0]