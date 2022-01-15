# Given an array of strings words representing an English Dictionary, return 
# the longest word in words that can be built one character at a time by other words 
# in words. 
# 
#  If there is more than one possible answer, return the longest word with the 
# smallest lexicographical order. If there is no answer, return the empty string. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", 
# "wo", "wor", and "worl".
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the 
# dictionary. However, "apple" is lexicographically smaller than "apply".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 30 
#  words[i] consists of lowercase English letters. 
#  
#  Related Topics Array Hash Table String Trie Sorting 👍 1200 👎 1243


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=lambda x: len(x))
        words_in_trie = {""}
        longest_word = ""

        for word in words:
            if word[:-1] not in words_in_trie:
                continue
            words_in_trie.add(word)
            word_len = len(word)
            longest_word_len = len(longest_word)
            if word_len > longest_word_len or (word_len == longest_word_len and word < longest_word):
                longest_word = word

        return longest_word
# leetcode submit region end(Prohibit modification and deletion)
