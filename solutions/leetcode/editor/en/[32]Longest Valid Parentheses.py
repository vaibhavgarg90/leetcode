# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#  
# 
#  Example 2: 
# 
#  
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#  
# 
#  Example 3: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] is '(', or ')'. 
#  
#  Related Topics String Dynamic Programming Stack 👍 6758 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        global_max = 0
        """
        "(()"
        ")()())"
        ")((()())))"
        ")())())"
        "()(()"
        """
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    global_max = max(global_max, i - stack[-1])
        return global_max
# leetcode submit region end(Prohibit modification and deletion)
