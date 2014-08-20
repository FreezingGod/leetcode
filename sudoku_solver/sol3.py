# very slow
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subs[i/3][j/3].add(board[i][j])
        full = set(str(i) for i in range(1,10))
        self.solve(board, rows, cols, subs, full)
    def solve(self, board, rows, cols, subs, full):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    candidates = full - rows[i] - cols[j] - subs[i/3][j/3]
                    if len(candidates) == 0:
                        return False
                    else:
                        for can in candidates:
                            board[i][j] = can
                            #printBoard(board)
                            rows[i].add(can)
                            cols[j].add(can)
                            subs[i/3][j/3].add(can)
                            #print i, j, can, candidates, rows[i], cols[j], subs[i/3][j/3]
                            if self.solve(board, rows, cols, subs, full):
                                return True
                            board[i][j] = '.'
                            rows[i].remove(can)
                            cols[j].remove(can)
                            subs[i/3][j/3].remove(can)
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
