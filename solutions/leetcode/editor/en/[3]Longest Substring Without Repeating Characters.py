# Given a string s, find the length of the longest substring without repeating 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 👍 19692 👎 902


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        global_max_start = global_max_end = local_max_start = local_max_end = 0
        d = {}  # captures the last index of each character seen so far
        for index, c in enumerate(s):
            prev_index = d.get(c, -1)
            if prev_index >= 0 and local_max_start <= prev_index <= local_max_end:
                # print(f"updating local_max_start from {local_max_start} to {prev_index + 1}")
                local_max_start = prev_index + 1
            local_max_end = index
            if (local_max_end - local_max_start) >= (global_max_end - global_max_start):
                # print(f"updating global_max_end from {global_max_end} to {local_max_end}")
                # print(f"updating global_max_start from {global_max_start} to {local_max_start}")
                global_max_end = local_max_end
                global_max_start = local_max_start
            d[c] = index
        return global_max_end - global_max_start + 1
# leetcode submit region end(Prohibit modification and deletion)
