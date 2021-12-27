# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 👍 10334 👎 412


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if (c == ')' and bracket != '(')\
                    or (c == '}' and bracket != '{')\
                    or (c == ']' and bracket != '['):
                    return False
        return not stack
# leetcode submit region end(Prohibit modification and deletion)
