class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a_set = set()
        b_set = set()
        c_set = set()
        for i in range(9):
            if i in (0, 3, 6):
                a_set.clear()
                b_set.clear()
                c_set.clear()

            row_set = set()
            column_set = set()
            for j in range(9):
                if 0 <= j <= 2:
                    if board[i][j] != '.':
                        if board[i][j] in a_set:
                            return False
                        a_set.add(board[i][j])
                if 3 <= j <= 5:
                    if board[i][j] != '.':
                        if board[i][j] in b_set:
                            return False
                        b_set.add(board[i][j])
                if 6 <= j <= 8:
                    if board[i][j] != '.':
                        if board[i][j] in c_set:
                            return False
                        c_set.add(board[i][j])

                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in column_set:
                        return False
                    column_set.add(board[j][i])
        return True
        


        