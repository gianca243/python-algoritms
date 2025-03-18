"""First idea"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [list() for i in range(n)]
        for j in range(n):
            for i in range(n-1, -1,-1):
                ans[j].append(matrix[i][j]) # y, x
        
        for i in range(n):
            matrix[i] = ans[i]