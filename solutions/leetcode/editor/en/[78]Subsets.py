# Given an integer array nums of unique elements, return all possible subsets (
# the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Backtracking Bit Manipulation 👍 8055 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

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

        return rec(0)
# leetcode submit region end(Prohibit modification and deletion)
