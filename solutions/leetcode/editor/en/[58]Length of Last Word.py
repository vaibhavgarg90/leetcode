# Given a string s consisting of some words separated by some number of spaces, 
# return the length of the last word in the string. 
# 
#  A word is a maximal substring consisting of non-space characters only. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only English letters and spaces ' '. 
#  There will be at least one word in s. 
#  
#  Related Topics String 👍 592 👎 53


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = cur_len = 0
        for c in s:
            if c == ' ':
                cur_len = 0
            else:
                cur_len += 1
                last_len = cur_len
        return last_len
# leetcode submit region end(Prohibit modification and deletion)
