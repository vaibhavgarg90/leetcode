# # Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2
# ] 
# # < nums[3].... 
# # 
# # You may assume the input array always has a valid answer. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: nums = [1,5,1,1,6,4]
# # Output: [1,6,1,5,1,4]
# # Explanation: [1,4,1,5,1,6] is also accepted.
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: nums = [1,3,2,2,3,1]
# # Output: [2,3,1,3,1,2]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # 1 <= nums.length <= 5 * 10⁴ 
# # 0 <= nums[i] <= 5000 
# # It is guaranteed that there will be an answer for the given input nums. 
# # 
# # 
# # 
# # Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
#  
# # Related Topics Array Divide and Conquer Sorting Quickselect 👍 1889 👎 763
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums_copy = nums[::]
        nums_copy.sort()
        j = n - 1
        for i in range(1, n, 2):
            nums[i] = nums_copy[j]
            j -= 1
        for i in range(0, n, 2):
            nums[i] = nums_copy[j]
            j -= 1
# leetcode submit region end(Prohibit modification and deletion)
