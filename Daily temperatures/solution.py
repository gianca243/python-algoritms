class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        response = [0]*len(temperatures)
        stack = []
        for index, item in enumerate(temperatures):
            while stack and item > temperatures[stack[-1]]:
                response[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return response