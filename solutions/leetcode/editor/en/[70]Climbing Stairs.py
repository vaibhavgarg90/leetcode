# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 👍 9617 👎 301


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 2)]
        # initialize base cases:
        # 1 solution for 1 step
        # 2 solutions for 2 steps
        dp[1] = 1
        dp[2] = 2

        def rec(x: int):
            if x == 0:
                return 0
            if dp[x]:
                return dp[x]
            dp[x - 1] = rec(x - 1)
            dp[x - 2] = rec(x - 2)
            return dp[x - 1] + dp[x - 2]

        return rec(n)
# leetcode submit region end(Prohibit modification and deletion)
