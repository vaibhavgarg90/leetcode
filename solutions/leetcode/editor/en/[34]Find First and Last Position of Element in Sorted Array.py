# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums is a non-decreasing array. 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Binary Search 👍 8496 👎 260


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = end = -1
        size = len(nums)
        low = 0
        high = size - 1
        # find the start
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if (mid == 0) or (nums[mid - 1] < nums[mid]):
                    start = mid
                    break
                else:
                    high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        # if start not found, means the element does not exist
        if start == -1:
            return [-1, -1]
        # find the end
        low = start
        high = size - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                if (mid == size - 1) or (nums[mid + 1] > nums[mid]):
                    end = mid
                    break
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [start, end]
# leetcode submit region end(Prohibit modification and deletion)
