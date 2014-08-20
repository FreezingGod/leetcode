class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # check row
                for k in range(9):
                    if k != j and board[i][k] == board[i][j]:
                        return False
                # check column
                for k in range(9):
                    if k != i and board[i][j] == board[k][j]:
                        return False
                # check 3x3 matrix
                idx1, idx2 = i/3, j/3
                for m in range(idx1*3, idx1*3+3):
                    for n in range(idx2*3, idx2*3+3):
                        if not (m == i and n == j) and board[m][n] == board[i][j]:
                            return False
        return True
