# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums. 
# 
#  
#  Example 1: 
#  Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#  Example 2: 
#  Input: nums = [1,1]
# Output: [2]
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 10⁵ 
#  1 <= nums[i] <= n 
#  
# 
#  
#  Follow up: Could you do it without extra space and in O(n) runtime? You may 
# assume the returned list does not count as extra space. 
#  Related Topics Array Hash Table 👍 5772 👎 352


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # move elements to their true position
        for i, num in enumerate(nums):
            true_position = num - 1
            while 0 <= true_position < n and nums[i] != nums[true_position]:
                nums[i], nums[true_position] = nums[true_position], nums[i]
                true_position = nums[i] - 1

        res = []
        # check all the indices at which expected number is not present
        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(i + 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
