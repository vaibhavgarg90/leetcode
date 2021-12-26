# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lower-case English letters. 
#  
#  Related Topics String 👍 6281 👎 2673


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs = sorted(strs, key=lambda x: len(x), reverse=False)
        lcp = strs[0]
        for i in range(1, len(strs), 1):
            x = strs[i]
            new_lcp = []
            for j, c1 in enumerate(lcp):
                c2 = x[j]
                if c1 == c2:
                    new_lcp.append(c1)
                else:
                    break
            if not new_lcp:
                return ""
            lcp = "".join(new_lcp)
        return lcp
# leetcode submit region end(Prohibit modification and deletion)
