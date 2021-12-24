# Given a string s, return the longest palindromic substring in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: "bb"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consist of only digits and English letters. 
#  
#  Related Topics String Dynamic Programming 👍 14851 👎 870


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = end = 0
        for index, c in enumerate(s):
            l1 = self.lp_util(s, index, index)
            l2 = self.lp_util(s, index, index + 1)
            _max = max(l1, l2)
            if _max > (end - start + 1):
                start = index - int((_max - 1) / 2)
                end = index + int(_max / 2)
        return s[start: end + 1]

    def lp_util(self, s: str, i: int, j: int) -> int:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1
# leetcode submit region end(Prohibit modification and deletion)
