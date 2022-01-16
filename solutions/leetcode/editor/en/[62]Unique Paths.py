# There is a robot on an m x n grid. The robot is initially located at the top-
# left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
# corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at 
# any point in time. 
# 
#  Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner. 
# 
#  The test cases are generated so that the answer will be less than or equal 
# to 2 * 10⁹. 
# 
#  
#  Example 1: 
# 
#  
# Input: m = 3, n = 7
# Output: 28
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach 
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  
#  Related Topics Math Dynamic Programming Combinatorics 👍 7611 👎 276


# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def rec(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            return rec(i, j + 1) + rec(i + 1, j)

        return rec(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
