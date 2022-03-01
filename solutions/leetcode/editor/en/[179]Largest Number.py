# Given a list of non-negative integers nums, arrange them such that they form 
# the largest number and return it. 
# 
#  Since the result may be very large, so you need to return a string instead 
# of an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,2]
# Output: "210"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 10⁹ 
#  
#  Related Topics String Greedy Sorting 👍 4523 👎 392


# leetcode submit region begin(Prohibit modification and deletion)
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_sort(num1, num2):
            x = int(str(num1) + str(num2))
            y = int(str(num2) + str(num1))
            if x > y:
                return -1
            elif x == y:
                return 0
            else:
                return 1

        nums = sorted(nums, key=functools.cmp_to_key(custom_sort))
        res = [""] * len(nums)
        has_non_zero = False
        for i, num in enumerate(nums):
            res[i] = str(num)
            if num > 0:
                has_non_zero = True
        return "".join(res) if has_non_zero else "0"
# leetcode submit region end(Prohibit modification and deletion)
