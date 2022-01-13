# Given an integer array nums of length n where all the integers of nums are in 
# the range [1, n] and each integer appears once or twice, return an array of all 
# the integers that appears twice. 
# 
#  You must write an algorithm that runs in O(n) time and uses only constant 
# extra space. 
# 
#  
#  Example 1: 
#  Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
#  Example 2: 
#  Input: nums = [1,1,2]
# Output: [1]
#  Example 3: 
#  Input: nums = [1]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= n 
#  Each element in nums appears once or twice. 
#  
#  Related Topics Array Hash Table 👍 5402 👎 231


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, num in enumerate(nums):
            true_position = nums[i] - 1
            while 0 <= true_position < n and nums[true_position] != nums[i]:
                nums[i], nums[true_position] = nums[true_position], nums[i]
                true_position = nums[i] - 1
        res = {0}
        for i, num in enumerate(nums):
            if num != i + 1:
                res.add(num)
        res.remove(0)
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)
