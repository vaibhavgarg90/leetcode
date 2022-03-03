# An integer array is called arithmetic if it consists of at least three 
# elements and if the difference between any two consecutive elements is the same. 
# 
#  
#  For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic 
# sequences. 
#  
# 
#  Given an integer array nums, return the number of arithmetic subarrays of 
# nums. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,
# 2,3,4] itself.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -1000 <= nums[i] <= 1000 
#  
#  Related Topics Array Dynamic Programming 👍 3518 👎 239


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = 0
        left = 0
        while left < (n - 2):
            right = left + 1
            diff = nums[right] - nums[left]
            while right < n and nums[right] - nums[right - 1] == diff:
                right += 1
            right -= 1
            if right - left >= 2:
                num = right - left
                res += (num * (num - 1)) // 2
            left = right
        return res
# leetcode submit region end(Prohibit modification and deletion)
