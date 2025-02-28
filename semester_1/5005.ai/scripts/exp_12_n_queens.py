from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    def solve(col, board, ans, lr, ud, ld, n):
        if col == n:
            ans.append([''.join(row) for row in board])
            return
        for row in range(n):
            if lr[row] == 0 and ld[row - col] == 0 and ud[row + col] == 0:
                board[row][col] = 'Q'
                lr[row] = 1
                ld[row - col] = 1
                ud[row + col] = 1
                solve(col + 1, board, ans, lr, ud, ld, n)
                board[row][col] = '.'
                lr[row] = 0
                ld[row - col] = 0
                ud[row + col] = 0
    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    leftrow = [0] * n
    upperDiagonal = [0] * (2 * n - 1)
    lowerDiagonal = [0] * (2 * n - 1)
    solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
    return ans