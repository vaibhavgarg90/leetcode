# We define the usage of capitals in a word to be right when one of the 
# following cases holds: 
# 
#  
#  All letters in this word are capitals, like "USA". 
#  All letters in this word are not capitals, like "leetcode". 
#  Only the first letter in this word is capital, like "Google". 
#  
# 
#  Given a string word, return true if the usage of capitals in it is right. 
# 
#  
#  Example 1: 
#  Input: word = "USA"
# Output: true
#  Example 2: 
#  Input: word = "FlaG"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 100 
#  word consists of lowercase and uppercase English letters. 
#  
#  Related Topics String 👍 1128 👎 331


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase_count = 0
        lowercase_count = 0
        for c in word:
            is_lowercase = c.lower() == c
            if is_lowercase:
                if uppercase_count > 1:
                    return False
                lowercase_count += 1
            else:
                if lowercase_count > 0:
                    return False
                uppercase_count += 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
