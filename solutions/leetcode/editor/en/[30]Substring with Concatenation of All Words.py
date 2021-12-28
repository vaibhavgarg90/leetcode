# You are given a string s and an array of strings words of the same length. 
# Return all starting indices of substring(s) in s that is a concatenation of each 
# word in words exactly once, in any order, and without any intervening characters. 
# 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" 
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lower-case English letters. 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 30 
#  words[i] consists of lower-case English letters. 
#  
#  Related Topics Hash Table String Sliding Window 👍 1642 👎 1710


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        word_count = len(words)
        word_count_size = word_size * word_count
        str_size = len(s)
        if str_size < word_count_size:
            return []
        indices = []
        for i in range(str_size - word_count_size + 1):
            _map = Counter(words)
            words_found = 0
            for j in range(i, i + word_count_size, word_size):
                cur_s = s[j: j + word_size]
                if cur_s in _map and _map[cur_s] > 0:
                    _map[cur_s] -= 1
                    words_found += 1
            if words_found == word_count:
                indices.append(i)
        return indices
# leetcode submit region end(Prohibit modification and deletion)
