# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division, and mod operator. 
# 
#  The integer division should truncate toward zero, which means losing its 
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be 
# truncated to -2. 
# 
#  Return the quotient after dividing dividend by divisor. 
# 
#  Note: Assume we are dealing with an environment that could only store 
# integers within the 32-bit signed integer range: [−2³¹, 2³¹ − 1]. For this problem, if 
# the quotient is strictly greater than 2³¹ - 1, then return 2³¹ - 1, and if the 
# quotient is strictly less than -2³¹, then return -2³¹. 
# 
#  
#  Example 1: 
# 
#  
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#  
# 
#  Example 2: 
# 
#  
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= dividend, divisor <= 2³¹ - 1 
#  divisor != 0 
#  
#  Related Topics Math Bit Manipulation 👍 2385 👎 8526


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        min_int = -2 ** 31
        max_int = 2 ** 31 - 1
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            tmp = b
            mul = 1
            while a >= tmp:
                a -= tmp
                res += mul
                mul += mul
                tmp += tmp
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
        if res < min_int:
            return min_int
        if res > max_int:
            return max_int
        return res
# leetcode submit region end(Prohibit modification and deletion)
