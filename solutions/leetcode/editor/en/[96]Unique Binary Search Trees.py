# Given an integer n, return the number of structurally unique BST's (binary 
# search trees) which has exactly n nodes of unique values from 1 to n. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: 5
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
#  1 <= n <= 19 
#  
#  Related Topics Math Dynamic Programming Tree Binary Search Tree Binary Tree ?
# ? 6764 👎 267


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:

        def memoization(f):
            dp = {0: 0, 1: 1, 2: 2}

            def inner(start, end):
                key = end - start + 1
                if key not in dp:
                    dp[key] = f(start, end)
                return dp[key]

            return inner

        @memoization
        def rec(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            count = 0
            for i in range(start, end + 1):
                l_count = max(1, rec(start, i - 1))
                r_count = max(1, rec(i + 1, end))
                count += l_count * r_count
            return count

        return rec(1, n)
# leetcode submit region end(Prohibit modification and deletion)
