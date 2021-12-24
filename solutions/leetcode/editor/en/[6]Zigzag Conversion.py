# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
# of rows like this: (you may want to display this pattern in a fixed font for 
# better legibility) 
# 
#  
# P   A   H   N
# A P L S I I G
# Y   I   R
#  
# 
#  And then read line by line: "PAHNAPLSIIGYIR" 
# 
#  Write the code that will take a string and make this conversion given a 
# number of rows: 
# 
#  
# string convert(string s, int numRows);
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#  
# 
#  Example 3: 
# 
#  
# Input: s = "A", numRows = 1
# Output: "A"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of English letters (lower-case and upper-case), ',' and '.'. 
#  1 <= numRows <= 1000 
#  
#  Related Topics String 👍 3119 👎 7339


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows <= 1:
            return s
        l: list[str] = []
        i = 0
        down = True
        for c in s:
            if len(l) <= i:
                l.insert(i, "")
            l[i] = l[i] + c
            i += 1 if down else -1
            if i % numRows == 0:
                if down:
                    down = False
                    i -= 2
                else:
                    down = True
                    i = 0
        # print(l)
        return "".join(l)
        
# leetcode submit region end(Prohibit modification and deletion)
