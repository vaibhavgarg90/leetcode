# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#  Example 2: 
#  Input: nums = [0]
# Output: [[],[0]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics Array Backtracking Bit Manipulation 👍 4115 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def append(num, next_power_sets):
            current_power_sets = []
            for power_set in next_power_sets:
                current_power_sets.append(power_set)
                current_power_set = [num]
                current_power_set.extend(power_set)
                current_power_sets.append(current_power_set)
            return current_power_sets

        def rec(i):
            if i == n:
                return [[]]
            return append(nums[i], rec(i + 1))

        def dedup(res):
            from itertools import groupby
            res = sorted(res)
            return [k for k, _ in groupby(res)]

        return dedup(rec(0))
# leetcode submit region end(Prohibit modification and deletion)
