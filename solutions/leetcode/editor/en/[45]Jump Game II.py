# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that 
# position. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  You can assume that you can always reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics Array Dynamic Programming Greedy 👍 6788 👎 261


# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def rec(i):
            if i >= n - 1:
                return 0
            j = nums[i]
            min_jumps = 10 ** 5
            while j > 0:
                min_jumps = min(min_jumps, rec(i + j))
                j -= 1
            return 1 + min_jumps

        if n == 1:
            return 0
        
        return rec(0)
# leetcode submit region end(Prohibit modification and deletion)
