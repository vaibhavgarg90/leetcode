# Given an m x n matrix, return all elements of the matrix in spiral order. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics Array Matrix Simulation 👍 5903 👎 766


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i = j = 0
        mini, maxi = 0, m - 1
        minj, maxj = 0, n - 1
        direction = 'R'
        while mini <= i <= maxi and minj <= j <= maxj:
            res.append(matrix[i][j])
            if direction == 'R':
                if j == maxj:
                    direction = 'D'
                    i += 1
                    mini += 1
                else:
                    j += 1
            elif direction == 'D':
                if i == maxi:
                    direction = 'L'
                    j -= 1
                    maxj -= 1
                else:
                    i += 1
            elif direction == 'L':
                if j == minj:
                    direction = 'U'
                    i -= 1
                    maxi -= 1
                else:
                    j -= 1
            else:
                if i == mini:
                    direction = 'R'
                    j += 1
                    minj += 1
                else:
                    i -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
