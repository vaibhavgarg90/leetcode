# Given an integer n, return true if it is a power of three. Otherwise, return 
# false. 
# 
#  An integer n is a power of three, if there exists an integer x such that n ==
#  3ˣ. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 27
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: n = 0
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: n = 9
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= n <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without loops/recursion? Related Topics Math 
# Recursion 👍 805 👎 102


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
# leetcode submit region end(Prohibit modification and deletion)
