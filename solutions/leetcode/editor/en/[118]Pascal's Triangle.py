# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
# 
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
#  Related Topics Array Dynamic Programming 👍 5002 👎 191


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows in (1, 2):
            return res[:numRows]
        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
# leetcode submit region end(Prohibit modification and deletion)
