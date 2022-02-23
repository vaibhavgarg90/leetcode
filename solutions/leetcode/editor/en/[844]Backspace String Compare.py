# Given two strings s and t, return true if they are equal when both are typed 
# into empty text editors. '#' means a backspace character. 
# 
#  Note that after backspacing an empty text, the text will continue empty. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 200 
#  s and t only contain lowercase letters and '#' characters. 
#  
# 
#  
#  Follow up: Can you solve it in O(n) time and O(1) space? 
#  Related Topics Two Pointers String Stack Simulation 👍 3584 👎 166


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        def populate(stack, s):
            for c in s:
                if c == "#" and stack:
                    stack.pop()
                elif c != "#":
                    stack.append(c)

        populate(s_stack, s)
        populate(t_stack, t)

        return "".join(s_stack) == "".join(t_stack)
# leetcode submit region end(Prohibit modification and deletion)
