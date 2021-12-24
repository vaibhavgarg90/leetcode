# Given a signed 32-bit integer x, return x with its digits reversed. If 
# reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed 
# or unsigned). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: x = -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: x = 120
# Output: 21
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
#  Related Topics Math 👍 6169 👎 8977


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        num: int = 0
        mul: int = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            num *= 10
            num += x % 10
            x = int(x / 10)
        num *= mul
        return num if -2 ** 31 <= num <= 2 ** 31 - 1 else 0
# leetcode submit region end(Prohibit modification and deletion)
