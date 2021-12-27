# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics String Dynamic Programming Backtracking 👍 10874 👎 425


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gp_util(nopen, nclose, s):
            if nopen == nclose == n:
                res.append(s)
                return

            if nopen < n:
                gp_util(nopen + 1, nclose, s + "(")

            if nclose < nopen:
                gp_util(nopen, nclose + 1, s + ")")

        gp_util(0, 0, "")
        return res
# leetcode submit region end(Prohibit modification and deletion)
