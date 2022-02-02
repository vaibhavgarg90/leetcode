# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s and p consist of lowercase English letters. 
#  
#  Related Topics Hash Table String Sliding Window 👍 6480 👎 241


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        res = []

        def get_index(c):
            return ord(c) - ord('a')

        def get_frequency(s: str):
            lst = [0] * 26
            for c in s:
                lst[get_index(c)] += 1
            return lst

        s_frequency = get_frequency(s[:n - 1])
        p_frequency_str = str(get_frequency(p))

        for i in range(n - 1, m):
            in_index = i
            out_index = i - n + 1
            s_frequency[get_index(s[in_index])] += 1
            if str(s_frequency) == p_frequency_str:
                res.append(out_index)
            s_frequency[get_index(s[out_index])] -= 1

        return res
# leetcode submit region end(Prohibit modification and deletion)
