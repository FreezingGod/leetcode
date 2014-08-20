class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.dfs(board)
    def isValid(self, board, value, m, n):
        for i in range(9):
            if board[m][i] == value or board[i][n] == value:
                return False
        for i in range(3):
            for j in range(3):
                if board[(m/3)*3+i][(n/3)*3+j] == value:
                    return False
        return True
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        if self.isValid(board, k, i, j):
                            board[i][j] = k
                            if self.dfs(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

def printBoard(board):
    for i in board:
        for j in i:
            print j,
        print
    print
def conBoard1(board):
    result = []
    for i in board:
        result.append([j for j in i])
    return result
def conBoard2(board):
    result = []
    for i in board:
        result.append(''.join(i))
    return result
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = conBoard1(board)
printBoard(board)
sol = Solution()
sol.solveSudoku(board)
printBoard(board)
