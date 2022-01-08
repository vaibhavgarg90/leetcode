# You are given a list of songs where the iᵗʰ song has a duration of time[i] 
# seconds. 
# 
#  Return the number of pairs of songs for which their total duration in 
# seconds is divisible by 60. Formally, we want the number of indices i, j such that i < 
# j with (time[i] + time[j]) % 60 == 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#  
# 
#  Example 2: 
# 
#  
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible 
# by 60.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= time.length <= 6 * 10⁴ 
#  1 <= time[i] <= 500 
#  
#  Related Topics Array Hash Table Counting 👍 2800 👎 107


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        buckets = [0 for _ in range(60)]
        for t in time:
            buckets[t % 60] += 1
        count = 0
        for i in range(1, 30):
            count += buckets[i] * buckets[60 - i]
        if buckets[0]:
            count += (buckets[0] * (buckets[0] - 1)) // 2
        if buckets[30]:
            count += (buckets[30] * (buckets[30] - 1)) // 2
        return count
# leetcode submit region end(Prohibit modification and deletion)
