# Given a pattern and a string s, find if s follows the same pattern. 
# 
#  Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length <= 300 
#  pattern contains only lower-case English letters. 
#  1 <= s.length <= 3000 
#  s contains only lowercase English letters and spaces ' '. 
#  s does not contain any leading or trailing spaces. 
#  All the words in s are separated by a single space. 
#  
#  Related Topics Hash Table String 👍 3064 👎 349


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        if len(pattern) != len(strs):
            return False
        pattern_to_word_dict = {}
        word_to_pattern_dict = {}
        for pat, word in zip(pattern, strs):
            if (pat in pattern_to_word_dict and word not in word_to_pattern_dict) or \
                (pat not in pattern_to_word_dict and word in word_to_pattern_dict):
                return False
            if pat in pattern_to_word_dict and word in word_to_pattern_dict and \
                (pattern_to_word_dict[pat] != word or word_to_pattern_dict[word] != pat):
                return False
            pattern_to_word_dict[pat] = word
            word_to_pattern_dict[word] = pat
        return True

# leetcode submit region end(Prohibit modification and deletion)
