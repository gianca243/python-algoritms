class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        columns = len(matrix[0])
        rows = len(matrix)
        ans_len = columns*rows
        ans = []
        up = 0
        down = rows-1
        left = 0
        right = columns-1

        x_move = 1
        y_move = 0

        x = 0
        y = 0
        while len(ans) < ans_len:
            ans.append(matrix[y][x])
            if x == right and y == up and x_move == 1:
                up += 1
                x_move = 0
                y_move = 1
            if x == right and y == down and y_move == 1:
                right -= 1
                x_move = -1
                y_move = 0
            if x == left and y == down and x_move == -1:
                down -= 1
                x_move = 0
                y_move = -1
            if x == left and y == up and y_move == -1:
                left += 1
                x_move = 1
                y_move = 0
            x += x_move
            y += y_move
        return ans

