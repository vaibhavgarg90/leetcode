# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
#  Related Topics Array Binary Search Matrix 👍 6125 👎 245


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid][0]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        i = low - 1

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[i][mid]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
# leetcode submit region end(Prohibit modification and deletion)
