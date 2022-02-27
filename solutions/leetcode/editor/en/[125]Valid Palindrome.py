# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric 
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 👍 3158 👎 4879


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        ord_0, ord_9 = ord('0'), ord('9')
        ord_A, ord_Z = ord('A'), ord('Z')
        ord_a, ord_z = ord('a'), ord('z')

        def convert(c):
            ord_c = ord(c)
            if ord_0 <= ord_c <= ord_9 or ord_A <= ord_c <= ord_Z or ord_a <= ord_c <= ord_z:
                return True, c.lower()
            return False, ''

        left, right = 0, n - 1
        while left < right:
            c1 = s[left]
            valid, c1 = convert(c1)
            if not valid:
                left += 1
                continue
            c2 = s[right]
            valid, c2 = convert(c2)
            if not valid:
                right -= 1
                continue
            if c1 != c2:
                return False
            left += 1
            right -= 1

        return True
# leetcode submit region end(Prohibit modification and deletion)
