# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 12208 👎 308


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        def dfs(i, j):
            grid[i][j] = "0"
            # left
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                dfs(i, j - 1)
            # up
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            # right
            if j + 1 < n and grid[i][j + 1] == "1":
                dfs(i, j + 1)
            # down
            if i + 1 < m and grid[i + 1][j] == "1":
                dfs(i + 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
# leetcode submit region end(Prohibit modification and deletion)
