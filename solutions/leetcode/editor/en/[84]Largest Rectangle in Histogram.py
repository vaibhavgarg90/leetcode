# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the 
# histogram. 
# 
#  
#  Example 1: 
# 
#  
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#  
# 
#  Example 2: 
# 
#  
# Input: heights = [2,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= heights.length <= 10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
#  Related Topics Array Stack Monotonic Stack 👍 8198 👎 126


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
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
