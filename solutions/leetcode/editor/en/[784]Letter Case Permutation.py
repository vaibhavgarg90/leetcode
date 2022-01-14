# Given a string s, you can transform every letter individually to be lowercase 
# or uppercase to create another string. 
# 
#  Return a list of all possible strings we could create. Return the output in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 12 
#  s consists of lowercase English letters, uppercase English letters, and 
# digits. 
#  
#  Related Topics String Backtracking Bit Manipulation 👍 2867 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)

        def append(c, next_permutations):
            current_permutations = [c.lower(), c.upper()] if c.isalpha() else [c]
            if not next_permutations:
                return current_permutations
            all_permutations = []
            for one_char in current_permutations:
                for permutation in next_permutations:
                    all_permutations.append(one_char + permutation)
            return all_permutations

        def rec(i):
            if i == n:
                return []
            return append(s[i], rec(i + 1))

        return rec(0)
# leetcode submit region end(Prohibit modification and deletion)
