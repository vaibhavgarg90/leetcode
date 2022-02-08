# Given a list of unique words, return all the pairs of the distinct indices (i,
#  j) in the given list, so that the concatenation of the two words words[i] + 
# words[j] is a palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 5000 
#  0 <= words[i].length <= 300 
#  words[i] consists of lower-case English letters. 
#  
#  Related Topics Array Hash Table String Trie 👍 2513 👎 221


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def is_palindrome(word):
            return word == word[::-1]

        _dict = {}
        res = []
        for i, word in enumerate(words):
            _dict[word] = i

        empty_index = _dict.get("", -1)

        for i, word in enumerate(words):
            if empty_index > -1 and empty_index != i and is_palindrome(word):
                res.append([empty_index, i])
            for j in range(len(word)):
                left, right = word[:j], word[j:]
                left_rev, right_rev = left[::-1], right[::-1]
                # palindrome => word + left_rev
                if left_rev in _dict and _dict[left_rev] != i and is_palindrome(right):
                    res.append([i, _dict[left_rev]])
                # palindrome => right_rev + word
                if right_rev in _dict and _dict[right_rev] != i and is_palindrome(left):
                    res.append([_dict[right_rev], i])

        return res
# leetcode submit region end(Prohibit modification and deletion)
