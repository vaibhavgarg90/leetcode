# Given an unsorted integer array nums, return the smallest missing positive 
# integer. 
# 
#  You must implement an algorithm that runs in O(n) time and uses constant 
# extra space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,0]
# Output: 3
#  Example 2: 
#  Input: nums = [3,4,-1,1]
# Output: 2
#  Example 3: 
#  Input: nums = [7,8,9,11,12]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
#  Related Topics Array Hash Table 👍 8011 👎 1205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def sol_o_n_time_o_n_space():
            """
            O(n) time
            O(n) space
            """
            _set = {x for x in nums if x > 0}
            for i in range(1, len(_set) + 2):
                if i not in _set:
                    return i

        """
        O(n) time
        O(1) space
        """
        size = len(nums)
        # try to arrange elements at their true position
        for i, num in enumerate(nums):
            true_position = num - 1
            while 0 <= true_position < size and nums[i] != nums[true_position]:
                nums[i], nums[true_position] = nums[true_position], nums[i]
                true_position = nums[i] - 1
        # find the first element that is out of order
        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        # all the elements are in order
        return size + 1

# leetcode submit region end(Prohibit modification and deletion)
