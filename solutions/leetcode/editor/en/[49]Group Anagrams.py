# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
#  Related Topics Hash Table String Sorting 👍 8067 👎 279


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}

        for _str in strs:
            lst = [0] * 26
            for c in _str:
                lst[ord(c) - ord('a')] += 1
            lst_str = str(lst)
            _dict_lst = _dict.get(lst_str, [])
            _dict_lst.append(_str)
            _dict[lst_str] = _dict_lst

        return list(_dict.values())
# leetcode submit region end(Prohibit modification and deletion)
