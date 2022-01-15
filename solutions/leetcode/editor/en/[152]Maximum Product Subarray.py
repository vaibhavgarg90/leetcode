# Given an integer array nums, find a contiguous non-empty subarray within the 
# array that has the largest product, and return the product. 
# 
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
#  
#  Related Topics Array Dynamic Programming 👍 9935 👎 313


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = local_max = global_min = local_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prev_local_min = local_min
            prev_local_max = local_max
            if num < 0:
                local_max = max(num, num * prev_local_min)
                local_min = min(num, num * prev_local_max)
            else:
                local_max = max(num, num * prev_local_max)
                local_min = min(num, num * prev_local_min)
            global_max = max(global_max, local_max)
            global_min = min(global_min, local_min)

        return global_max
# leetcode submit region end(Prohibit modification and deletion)
