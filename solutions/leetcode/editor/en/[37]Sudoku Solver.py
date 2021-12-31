# Write a program to solve a Sudoku puzzle by filling the empty cells. 
# 
#  A sudoku solution must satisfy all of the following rules: 
# 
#  
#  Each of the digits 1-9 must occur exactly once in each row. 
#  Each of the digits 1-9 must occur exactly once in each column. 
#  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-
# boxes of the grid. 
#  
# 
#  The '.' character indicates empty cells. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5
# ",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".
# ",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".
# ","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5
# "],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4
# ","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3
# "],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],[
# "9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3",
# "4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is 
# shown below:
# 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit or '.'. 
#  It is guaranteed that the input board has only one solution. 
#  
#  Related Topics Array Backtracking Matrix 👍 4216 👎 134c


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(l: List[str]):
            _set = {'.'}
            for s in l:
                if s == '.':
                    continue
                if s in _set:
                    return False
                _set.add(s)
            return True, _set

        def get_nums_in_row(i: int):
            return board[i]

        def get_nums_in_col(j: int):
            l: List[str] = []
            for i in range(9):
                l.append(board[i][j])
            return l

        def get_nums_in_grid(i: int, j: int):
            start_i = 3 * (i // 3)
            start_j = 3 * (j // 3)

            l: List[str] = []
            for x in range(start_i, start_i + 3):
                for y in range(start_j, start_j + 3):
                    l.append(board[x][y])
            return l

        def next_i_j(i: int, j: int):
            if j == 8:
                i += 1
                j = 0
            else:
                j += 1
            return i, j

        def sudoko_solver(i: int, j: int):
            if i > 8:
                return True

            val = board[i][j]
            if val != '.':
                i_next, j_next = next_i_j(i, j)
                return sudoko_solver(i_next, j_next)

            _set = {'.'}
            _set.update(get_nums_in_row(i))
            _set.update(get_nums_in_col(j))
            _set.update(get_nums_in_grid(i, j))

            for str_num in [str(x) for x in range(1, 10) if str(x) not in _set]:
                board[i][j] = str_num
                i_next, j_next = next_i_j(i, j)
                if sudoko_solver(i_next, j_next):
                    return True

            board[i][j] = '.'
            return False

        sudoko_solver(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
