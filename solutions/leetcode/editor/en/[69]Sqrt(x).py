# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and 
# only the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part 
# is truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
#  Related Topics Math Binary Search 👍 3372 👎 3026


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x

        low, high = 1, 2 ** 30

        while low < high:
            mid = (low + high) // 2
            y = mid * mid
            y_next = (mid + 1) * (mid + 1)
            if y == x or y < x < y_next:
                low = high = mid
            elif y < x:
                low = mid + 1
            elif y > x:
                high = mid - 1

        return low
# leetcode submit region end(Prohibit modification and deletion)
