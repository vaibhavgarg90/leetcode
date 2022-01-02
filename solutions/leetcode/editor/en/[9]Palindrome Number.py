# Given an integer x, return true if x is palindrome integer. 
# 
#  An integer is a palindrome when it reads the same backward as forward. 
# 
#  
#  For example, 121 is a palindrome while 123 is not. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string? 
# Related Topics Math 👍 4652 👎 1952


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        reverse = 0
        num = x
        while num > 0:
            reverse *= 10
            reverse += num % 10
            num //= 10
        return x == reverse
# leetcode submit region end(Prohibit modification and deletion)
