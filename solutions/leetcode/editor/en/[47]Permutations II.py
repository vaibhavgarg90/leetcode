# Given a collection of numbers, nums, that might contain duplicates, return 
# all possible unique permutations in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics Array Backtracking 👍 4252 👎 88


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def append(num, next_permutations):
            if not next_permutations:
                return [[num]]
            current_permutations = []
            m = len(next_permutations[0])
            for permutation in next_permutations:
                for i in range(m + 1):
                    current_permutation = permutation[::]
                    current_permutation.insert(i, num)
                    current_permutations.append(current_permutation)
            return current_permutations

        def rec(i):
            if i == n:
                return []
            return append(nums[i], rec(i + 1))

        def dedup(res):
            from itertools import groupby
            res = sorted(res)
            return [k for k, _ in groupby(res)]

        return dedup(rec(0))
# leetcode submit region end(Prohibit modification and deletion)
