# A transformation sequence from word beginWord to word endWord using a 
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#  
# 
#  
#  Every adjacent pair of words differs by a single letter. 
#  Every si for 1 <= i <= k is in wordList. Note that beginWord does not need 
# to be in wordList. 
#  sk == endWord 
#  
# 
#  Given two words, beginWord and endWord, and a dictionary wordList, return 
# the number of words in the shortest transformation sequence from beginWord to 
# endWord, or 0 if no such sequence exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog",
# "lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -
# > "dog" -> cog", which is 5 words long.
#  
# 
#  Example 2: 
# 
#  
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog",
# "lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no 
# valid transformation sequence.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= beginWord.length <= 10 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord, endWord, and wordList[i] consist of lowercase English letters. 
#  beginWord != endWord 
#  All the words in wordList are unique. 
#  
#  Related Topics Hash Table String Breadth-First Search 👍 7222 👎 1592


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        n = len(beginWord)

        res = 0
        q = [beginWord]

        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                word = q.pop(0)
                for i in range(n):
                    for j in range(26):
                        next_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                        if next_word == endWord:
                            return res + 1
                        if next_word in word_set:
                            q.append(next_word)
                            word_set.remove(next_word)
        return 0
# leetcode submit region end(Prohibit modification and deletion)
