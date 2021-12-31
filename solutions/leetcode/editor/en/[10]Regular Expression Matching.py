# Given an input string s and a pattern p, implement regular expression 
# matching with support for '.' and '*' where: 
# 
#  
#  '.' Matches any single character. 
#  '*' Matches zero or more of the preceding element. 
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, 
# by repeating 'a' once, it becomes "aa".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 30 
#  s contains only lowercase English letters. 
#  p contains only lowercase English letters, '.', and '*'. 
#  It is guaranteed for each appearance of the character '*', there will be a 
# previous valid character to match. 
#  
#  Related Topics String Dynamic Programming Recursion 👍 7259 👎 996


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                cur_p = p[i - 1]
                cur_s = s[j - 1]
                # base case :- no string and pattern to match
                if i == 0 and j == 0:
                    dp[0][0] = True
                # no pattern :- all the pattern matching fails
                elif i == 0:
                    dp[0][j] = False
                # no string :- all the pattern matching fails
                # special case :- "*" (since it can pass with 0 character match as well)
                elif j == 0:
                    dp[i][0] = dp[i - 2][0] if cur_p == '*' else False
                # if current pattern to match is "*"
                # case 1 :- without matching anything (dp[i-2][j])
                # case 2 :- with matching with previous pattern (dp[i][j-1])
                elif cur_p == '*':
                    dp[i][j] = dp[i - 2][j]
                    prev_p = p[i - 2]
                    if not dp[i][j] and prev_p in ('.', cur_s):
                        dp[i][j] = dp[i][j - 1]
                # case 1 :- current pattern is a match
                # case 2 :- current pattern is not a match
                else:
                    dp[i][j] = dp[i - 1][j - 1] if cur_p in ('.', cur_s) else False
        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
