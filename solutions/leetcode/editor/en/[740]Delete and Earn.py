# You are given an integer array nums. You want to maximize the number of 
# points you get by performing the following operation any number of times: 
# 
#  
#  Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must 
# delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
#  
#  
# 
#  Return the maximum number of points you can earn by applying the above 
# operation some number of times. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# 
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
#  Related Topics Array Hash Table Dynamic Programming 👍 2938 👎 191


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_freq = [0]
        for i in range(nums[-1]):
            nums_freq.append(0)
        for i, num in enumerate(nums):
            nums_freq[num] += num
        dp = [0, nums_freq[0]]
        for i in range(1, len(nums_freq)):
            val = max(dp[i], dp[i - 1] + nums_freq[i])
            dp.append(val)
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
