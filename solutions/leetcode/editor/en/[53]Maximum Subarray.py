# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum. 
# 
#  A subarray is a contiguous part of an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
#  Related Topics Array Divide and Conquer Dynamic Programming 👍 17205 👎 814


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = local_max = -10 ** 5
        for num in nums:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
        return global_max
# leetcode submit region end(Prohibit modification and deletion)
