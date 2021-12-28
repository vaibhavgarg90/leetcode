# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 10⁴ 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 3291 👎 3073


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        needle_size = len(needle)
        for i in range(len(haystack)):
            comp = haystack[i: i + needle_size]
            # print(f"i = {i}, comp = {comp}")
            if needle == comp:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
