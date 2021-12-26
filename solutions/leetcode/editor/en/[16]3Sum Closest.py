# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target. 
# 
#  Return the sum of the three integers. 
# 
#  You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,0], target = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Two Pointers Sorting 👍 4837 👎 222


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = closest_sum = 10 ** 5
        nums = sorted(nums)
        size = len(nums)
        for i, x in enumerate(nums):
            j = i + 1
            k = size - 1
            while j < k:
                y = nums[j]
                z = nums[k]
                _sum = x + y + z
                diff = target - _sum
                if diff == 0:
                    return target
                if _sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                    closest_sum = _sum
        return closest_sum
# leetcode submit region end(Prohibit modification and deletion)
