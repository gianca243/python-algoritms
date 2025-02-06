"""
My approach
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for __ in range(numRows)]
        row = 0
        movement = 1
        for character in s:
            result[row].append(character)
            if row == numRows - 1:
                movement = -1
            elif row == 0 :
                movement = 1
            elif numRows == 1:
                movement = 0
            row += movement
        for index, _list in enumerate(result):
            result[index] = "".join(_list)
        new_result = ""
        for _row in result:
            new_result += _row
        return new_result
