# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
#  Related Topics Array Hash Table Union Find 👍 7924 👎 353


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = {}
        for num in nums:
            count = map.get(num - 1, 0)
            map[num] = count + 1
        max_count = 0
        for num, count in map.items():
            # if this is not the end of the sequence, continue
            if num + 1 in map:
                continue
            cur_count = map.get(num)
            prev_num = num - cur_count
            while prev_num in map:
                prev_count = map[prev_num]
                cur_count += prev_count
                prev_num -= prev_count
            max_count = max(max_count, cur_count)
        return max_count
# leetcode submit region end(Prohibit modification and deletion)
