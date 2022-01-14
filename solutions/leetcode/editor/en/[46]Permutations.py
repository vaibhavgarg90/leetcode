# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
#  Related Topics Array Backtracking 👍 8665 👎 169


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

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

        return rec(0)
# leetcode submit region end(Prohibit modification and deletion)
