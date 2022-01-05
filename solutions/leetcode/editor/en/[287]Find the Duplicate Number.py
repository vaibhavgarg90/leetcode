# Given an array of integers nums containing n + 1 integers where each integer 
# is in the range [1, n] inclusive. 
# 
#  There is only one repeated number in nums, return this repeated number. 
# 
#  You must solve the problem without modifying the array nums and uses only 
# constant extra space. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,4,2,2]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,1,3,4,2]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁵ 
#  nums.length == n + 1 
#  1 <= nums[i] <= n 
#  All the integers in nums appear only once except for precisely one integer 
# which appears two or more times. 
#  
# 
#  
#  Follow up: 
# 
#  
#  How can we prove that at least one duplicate number must exist in nums? 
#  Can you solve the problem in linear runtime complexity? 
#  
#  Related Topics Array Two Pointers Binary Search Bit Manipulation 👍 10831 👎 
# 1129


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        def solve_by_modifying_list():
            # sort the list and find the first out of order element
            for i, num in enumerate(nums):
                true_position = num - 1
                while 0 <= true_position < n and nums[i] != nums[true_position]:
                    nums[i], nums[true_position] = nums[true_position], nums[i]
                    true_position = nums[i] - 1

            for i, num in enumerate(nums):
                if i + 1 != num:
                    return num

            return -1

        # the idea is derived from finding the intersection point in a linked list
        # check: https://keithschwarz.com/interesting/code/?dir=find-duplicate
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
# leetcode submit region end(Prohibit modification and deletion)
