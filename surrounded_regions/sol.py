class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        if not m: return
        n = len(board[0])
        if not n: return
        for i in range(m):
            if board[i][0] == 'O':
                self.mark(board, m, n, i, 0)
            if board[i][n-1] == 'O':
                self.mark(board, m, n, i, n-1)
        for i in range(n):
            if board[0][i] == 'O':
                self.mark(board, m, n, 0, i)
            if board[m-1][i] == 'O':
                self.mark(board, m, n, m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'
    def mark(self, board, m, n, i, j):
        board[i][j] = '1'
        if i-1 >= 0 and board[i-1][j] == 'O':
            self.mark(board, m, n, i-1, j)
        if i+1 < m and board[i+1][j] == 'O':
            self.mark(board, m, n, i+1, j)
        if j-1 >= 0 and board[i][j-1] == 'O':
            self.mark(board, m, n, i, j-1)
        if j+1 < n and board[i][j+1] == 'O':
            self.mark(board, m, n, i, j+1)
def printBoard(b):
    for l in b:
        print ''.join(l)
    print
board = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"]
b = []
for i in board:
    b.append([j for j in i])
printBoard(b)
sol = Solution()
sol.solve(b)
printBoard(b)
