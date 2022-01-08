# Given an integer array nums, return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i]. 
# 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
# 
#  You must write an algorithm that runs in O(n) time and without using the 
# division operation. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#  Example 2: 
#  Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#  
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
#  
# 
#  
#  Follow up: Can you solve the problem in O(1) extra space complexity? (The 
# output array does not count as extra space for space complexity analysis.) 
#  Related Topics Array Prefix Sum 👍 10513 👎 664


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        prefix = suffix = 1
        # prefix multiplication
        for i in range(0, n, 1):
            res[i] = prefix
            prefix *= nums[i]
        # suffix multiplication
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
# leetcode submit region end(Prohibit modification and deletion)
