# You are given a rows x cols matrix grid representing a field of cherries 
# where grid[i][j] represents the number of cherries that you can collect from the (i, 
# j) cell. 
# 
#  You have two robots that can collect cherries for you: 
# 
#  
#  Robot #1 is located at the top-left corner (0, 0), and 
#  Robot #2 is located at the top-right corner (0, cols - 1). 
#  
# 
#  Return the maximum number of cherries collection using both robots by 
# following the rules below: 
# 
#  
#  From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (
# i + 1, j + 1). 
#  When any robot passes through a cell, It picks up all cherries, and the cell 
# becomes an empty cell. 
#  When both robots stay in the same cell, only one takes the cherries. 
#  Both robots cannot move outside of the grid at any moment. 
#  Both robots should reach the bottom row in grid. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue 
# respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0]
# ,[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue 
# respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == grid.length 
#  cols == grid[i].length 
#  2 <= rows, cols <= 70 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics Array Dynamic Programming Matrix 👍 1469 👎 13


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROW_NUM = len(grid)
        COL_NUM = len(grid[0])

        dp = [[[0] * COL_NUM for _ in grid[0]] for _ in grid]
        # fulfill dp of the last row
        for i in range(COL_NUM):
            for j in range(COL_NUM):
                dp[-1][i][j] = grid[-1][i] if i == j else grid[-1][i] + grid[-1][j]

        # from the second last row to the first row
        for k in range(ROW_NUM - 2, -1, -1):
            row = grid[k]
            for i in range(COL_NUM):
                # for every (i, j, k), dp[k][i][j] == dp[k][j][i]
                # so we only need to find the answer for j >= i
                for j in range(i, COL_NUM):
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= i + di < COL_NUM and 0 <= j + dj < COL_NUM:
                                if i == j:  # they can only pickup once
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i])
                                else:
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i] + row[j])
        return dp[0][0][COL_NUM - 1]
# leetcode submit region end(Prohibit modification and deletion)
