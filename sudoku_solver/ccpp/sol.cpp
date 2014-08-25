#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char> > &board) {
        dfs(board);
    }
    
    bool dfs(vector<vector<char> > &board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (check(board, i, j, c)) {
                            board[i][j] = c;
                            if (dfs(board)) {
                                return true;
                            } else {
                                board[i][j] = '.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    bool check(vector<vector<char> > &board, int m, int n, char candidate) {
        for (int i = 0; i < 9; i++) {
            if (i != n && board[m][i] == candidate)
                return false;
        }
        for (int i = 0; i < 9; i++) {
            if (i != m && board[i][n] == candidate)
                return false;
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (m!= m/3*3+i && n != n/3*3+j && board[m/3*3+i][n/3*3+j] == candidate)
                    return false;
            }
        }
        return true;
    }
};

