# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules: 
# 
#  
#  Each row must contain the digits 1-9 without repetition. 
#  Each column must contain the digits 1-9 without repetition. 
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
# without repetition. 
#  
# 
#  Note: 
# 
#  
#  A Sudoku board (partially filled) could be valid but is not necessarily 
# solvable. 
#  Only the filled cells need to be validated according to the mentioned rules. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner 
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is 
# invalid.
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit 1-9 or '.'. 
#  
#  Related Topics Array Hash Table Matrix 👍 4080 👎 651


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid(l: List[str]):
            _set = {""}
            for s in l:
                if s == '.':
                    continue
                if s in _set:
                    # print(f"{l = }")
                    return False
                _set.add(s)
            return True

        # validate rows
        for l in board:
            if not is_valid(l):
                return False

        # validate columns
        for j in range(9):
            l = []
            for i in range(9):
                l.append(board[i][j])
            if not is_valid(l):
                return False

        # validate 3 X 3 grids
        ll = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                index = (3 * (((i * 9) + j) // 27)) + (j // 3)
                # print(f"{i = } {j = } {index = }")
                ll[index].append(board[i][j])
        for l in ll:
            if not is_valid(l):
                return False

        # all checks passed
        return True
# leetcode submit region end(Prohibit modification and deletion)
