# Given an m x n grid of characters board and a string word, return true if 
# word exists in the grid. 
# 
#  The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter 
# cell may not be used more than once. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCCED"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "SEE"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCB"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board and word consists of only lowercase and uppercase English letters. 
#  
# 
#  
#  Follow up: Could you use search pruning to make your solution faster with a 
# larger board? 
#  Related Topics Array Backtracking Matrix 👍 8080 👎 304


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        x = len(word)

        """
        [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
        "AAAAAAAAAAAAAAB"
        
        [["b","b","b","a","b","b"],["b","a","b","b","a","a"],["b","a","b","a","a","a"],["a","a","a","a","b","a"],["a","a","b","b","b","a"],["a","a","b","b","a","a"]]
				"abbbbaabbbbb"
        """

        def dfs(i, j, k, used):
            # at least one character match has been found
            # tries to match as many characters as possible
            if k == x:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            index = i * n + j
            if index in used:
                return False
            k += 1
            used.add(index)
            val = dfs(i, j + 1, k, used) or dfs(i + 1, j, k, used) or dfs(i, j - 1, k, used) or dfs(i - 1, j, k, used)
            used.remove(index)
            return val

        def rec():
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        index = i * n + j
                        if dfs(i, j + 1, 1, {index}):
                            return True
                        if dfs(i + 1, j, 1, {index}):
                            return True
                        if dfs(i, j - 1, 1, {index}):
                            return True
                        if dfs(i - 1, j, 1, {index}):
                            return True
            return False

        return rec()
# leetcode submit region end(Prohibit modification and deletion)
