# Given a binary array nums, return the maximum length of a contiguous subarray 
# with an equal number of 0 and 1. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number 
# of 0 and 1.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal 
# number of 0 and 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] is either 0 or 1. 
#  
#  Related Topics Array Hash Table Prefix Sum 👍 4110 👎 174


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        prefix_sum = 0
        _dict = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in _dict:
                max_len = max(max_len, i - _dict[prefix_sum])
            else:
                _dict[prefix_sum] = i
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
