# Given an array of integers nums and an integer limit, return the size of the 
# longest non-empty subarray such that the absolute difference between any two 
# elements of this subarray is less than or equal to limit. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute 
# diff is |2-7| = 5 <= 5.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁹ 
#  0 <= limit <= 10⁹ 
#  
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Ordered Set 
# Monotonic Queue 👍 1935 👎 83


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        if n == 1:
            return 1

        increasing_q = []
        decreasing_q = []

        max_len = 0
        left, right = 0, 0

        while right < n:
            num = nums[right]
            while increasing_q and nums[increasing_q[-1]] > num:
                increasing_q.pop()
            increasing_q.append(right)
            while decreasing_q and nums[decreasing_q[-1]] < num:
                decreasing_q.pop()
            decreasing_q.append(right)

            min_elem = nums[increasing_q[0]]
            max_elem = nums[decreasing_q[0]]
            if max_elem - min_elem <= limit:
                max_len = max(max_len, right - left + 1)
            else:
                left += 1
                while increasing_q and left > increasing_q[0]:
                    increasing_q.pop(0)
                while decreasing_q and left > decreasing_q[0]:
                    decreasing_q.pop(0)
            right += 1

        return max_len
# leetcode submit region end(Prohibit modification and deletion)
