# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return the number of distinct solutions to the n-queens 
# puzzle. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 👍 1513 👎 208


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n <= 3:
            return 0

        self.res = 0

        _range_n = list(range(n))
        empty_board = [[0 for _ in _range_n] for _ in _range_n]

        def get_possible_cols(board, row):
            cols = {i for i in _range_n}

            # check vertically above
            for c in _range_n:
                for r in range(row):
                    if board[r][c] == 1:
                        cols.discard(c)

            # check diagonals
            for c in _range_n:
                r = row - 1
                c1 = c - 1
                c2 = c + 1
                while True:
                    if r not in _range_n:
                        break
                    if c1 in _range_n and board[r][c1] == 1:
                        cols.discard(c)
                    if c2 in _range_n and board[r][c2] == 1:
                        cols.discard(c)
                    r -= 1
                    c1 -= 1
                    c2 += 1

            return cols

        def rec(board, row):
            for col in get_possible_cols(board, row):
                board[row][col] = 1
                if row == n - 1:
                    self.res += 1
                else:
                    rec(board, row + 1)
                board[row][col] = 0

        rec(empty_board, 0)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
