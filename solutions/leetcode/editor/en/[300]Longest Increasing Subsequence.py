# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  A subsequence is a sequence that can be derived from an array by deleting 
# some or no elements without changing the order of the remaining elements. For 
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
#  Related Topics Array Binary Search Dynamic Programming 👍 10234 👎 207


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        _max = 1

        for i in range(1, n):
            num = nums[i]
            for j in range(0, i):
                if num > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            _max = max(_max, dp[i])

        return _max
# leetcode submit region end(Prohibit modification and deletion)
