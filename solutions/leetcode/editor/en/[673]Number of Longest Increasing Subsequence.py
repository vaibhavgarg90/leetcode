# Given an integer array nums, return the number of longest increasing 
# subsequences. 
# 
#  Notice that the sequence has to be strictly increasing. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 
# 3, 5, 7].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, 
# and there are 5 subsequences' length is 1, so output 5.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  -10⁶ <= nums[i] <= 10⁶ 
#  
#  Related Topics Array Dynamic Programming Binary Indexed Tree Segment Tree 👍 
# 3217 👎 160


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1) for _ in range(n)]
        for i in range(1, n):
            cur_len_lis = 1
            cur_count_lis = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if cur_len_lis < 1 + dp[j][0]:
                        cur_len_lis = 1 + dp[j][0]
                        cur_count_lis = dp[j][1]
                    elif cur_len_lis == 1 + dp[j][0]:
                        cur_count_lis += dp[j][1]
            dp[i] = (cur_len_lis, cur_count_lis)
        len_lis = 1
        count_lis = 1
        for i in range(1, n):
            if dp[i][0] > len_lis:
                len_lis = dp[i][0]
                count_lis = dp[i][1]
            elif dp[i][0] == len_lis:
                count_lis += dp[i][1]
        return count_lis
# leetcode submit region end(Prohibit modification and deletion)
