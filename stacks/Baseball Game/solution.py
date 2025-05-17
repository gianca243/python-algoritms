class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for item in operations:
            if item == "+":
                stack.append(stack[-2]+stack[-1])
            elif item == "D":
                stack.append(stack[-1]*2)
            elif item == "C":
                stack.pop()
            else:
                stack.append(int(item))
            print(stack)
        return sum(stack)