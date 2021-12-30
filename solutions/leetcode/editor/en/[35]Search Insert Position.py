# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be if it were 
# inserted in order. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums contains distinct values sorted in ascending order. 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Binary Search 👍 6119 👎 358


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        low = 0
        high = size - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return (mid + 1) if nums[mid] < target else mid
# leetcode submit region end(Prohibit modification and deletion)
