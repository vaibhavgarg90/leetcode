# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics Array Backtracking 👍 4148 👎 112


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        size = len(candidates)
        subset = []

        def dfs(i):
            if sum(subset) == target:
                res.append(subset[::])

            if i >= size or sum(subset) > target:
                return

            candidate = candidates[i]

            # include the element
            if (sum(subset) + candidate) <= target:
                subset.append(candidate)
                dfs(i + 1)
                # skip duplicate elements
                i += 1
                while i < size and candidates[i] == candidate:
                    i += 1
                # exclude the element
                subset.pop()
                if i < size and ((sum(subset) + candidates[i]) <= target):
                    dfs(i)

        def dedup(l: List[List[int]]):
            if not l:
                return l
            l.sort()
            try:
                import itertools
            except Exception:
                pass
            return [x for x, _ in itertools.groupby(l)]

        dfs(0)
        return dedup(res)
# leetcode submit region end(Prohibit modification and deletion)
