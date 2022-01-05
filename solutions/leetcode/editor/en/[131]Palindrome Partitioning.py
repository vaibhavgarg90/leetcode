# Given a string s, partition s such that every substring of the partition is a 
# palindrome. Return all possible palindrome partitioning of s. 
# 
#  A palindrome string is a string that reads the same backward as forward. 
# 
#  
#  Example 1: 
#  Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#  Example 2: 
#  Input: s = "a"
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s contains only lowercase English letters. 
#  
#  Related Topics String Dynamic Programming Backtracking 👍 5139 👎 155


# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache
from itertools import groupby


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def dedup(res: List[List[str]]):
            res.sort()
            return [k for k, _ in groupby(res)]

        @cache
        def is_palindrome(s1: str) -> bool:
            return s1 == s1[::-1]

        @cache
        def rec(start: int, end: int):
            if start == end:
                return [[s[start]]]

            res = []
            for i in range(start, end):
                prefix_res = rec(start, i)
                suffix_res = rec(i + 1, end)
                for p_res in prefix_res:
                    for s_res in suffix_res:
                        merged_res = [] + p_res + s_res
                        res.append(merged_res)

            if is_palindrome(s[start: end + 1]):
                res.append([s[start: end + 1]])

            return dedup(res)

        return rec(0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
