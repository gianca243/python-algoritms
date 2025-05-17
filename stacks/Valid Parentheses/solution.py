class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p = {"(", "{", "["}
        for item in s:
            n = len(stack)
            if item in open_p:
                stack.append(item)
            elif n > 0 and item == "}" and stack[-1] == "{":
                stack.pop()
            elif n > 0 and item == "]" and stack[-1] == "[":
                stack.pop()
            elif n > 0 and item == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True