# Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
# rectangle containing only 1's and return its area. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1",
# "1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [["0"]]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [["1"]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == matrix.length 
#  cols == matrix[i].length 
#  1 <= row, cols <= 200 
#  matrix[i][j] is '0' or '1'. 
#  
#  Related Topics Array Dynamic Programming Stack Matrix Monotonic Stack 👍 5986
#  👎 101


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maximal_rectangle = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                prev_val = 0 if i == 0 else int(matrix[i - 1][j])
                row[j] = 0 if val == "0" else 1 + prev_val
            maximal_rectangle = max(maximal_rectangle, self.largestRectangleArea(row))
        return maximal_rectangle

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_rect_area = 0
        for i, height in enumerate(heights):
            start_index = i
            while stack and stack[-1][0] > height:
                prev_height, prev_start_index = stack.pop()
                cur_rect_area = prev_height * (i - prev_start_index)
                max_rect_area = max(max_rect_area, cur_rect_area)
                start_index = prev_start_index
            if not stack or height > stack[-1][0]:
                stack.append((height, start_index))
        while stack:
            prev_height, prev_start_index = stack.pop()
            cur_rect_area = prev_height * (n - prev_start_index)
            max_rect_area = max(max_rect_area, cur_rect_area)
        return max_rect_area
# leetcode submit region end(Prohibit modification and deletion)
