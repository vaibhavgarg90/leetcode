# Implement next permutation, which rearranges numbers into the 
# lexicographically next greater permutation of numbers. 
# 
#  If such an arrangement is impossible, it must rearrange it to the lowest 
# possible order (i.e., sorted in ascending order). 
# 
#  The replacement must be in place and use only constant extra memory. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1]
# Output: [1,2,3]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,1,5]
# Output: [1,5,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics Array Two Pointers 👍 8114 👎 2742


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1:
            return
        i = size - 1
        # find the two consecutive indices from last where elements are in the ascending order
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # all the elements are arranged in the non-ascending order
        # next permutation will be all the elements arranged in the ascending order
        if i == 0:
            nums.reverse()
            return
        j = i - 1  # this is the index at which exchange needs to happen
        k = size - 1
        # figure out the element from the last that can be replaced by the element at index j
        while nums[k] <= nums[j]:
            k -= 1
        # exchange elements at indices j and k
        nums[j], nums[k] = nums[k], nums[j]
        # reverse the order of the elements starting from index i
        nums[i:] = nums[i:][::-1]
# leetcode submit region end(Prohibit modification and deletion)
