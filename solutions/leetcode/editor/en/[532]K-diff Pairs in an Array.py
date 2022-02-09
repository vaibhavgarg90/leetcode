# Given an array of integers nums and an integer k, return the number of unique 
# k-diff pairs in the array. 
# 
#  A k-diff pair is an integer pair (nums[i], nums[j]), where the following are 
# true: 
# 
#  
#  0 <= i < j < nums.length 
#  |nums[i] - nums[j]| == k 
#  
# 
#  Notice that |val| denotes the absolute value of val. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of 
# unique pairs.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) 
# and (4, 5).
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁷ <= nums[i] <= 10⁷ 
#  0 <= k <= 10⁷ 
#  
#  Related Topics Array Hash Table Two Pointers Binary Search Sorting 👍 1930 👎
#  1880


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        _dict = {}
        for num in nums:
            _dict[num] = _dict.get(num, 0) + 1

        res = 0
        for key, val in _dict.items():
            if k == 0:
                _dict[key] = _dict[key] - 1
            if _dict.get(key + k, 0) > 0:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
