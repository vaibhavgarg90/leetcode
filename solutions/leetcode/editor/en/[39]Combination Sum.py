# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order. 
# 
#  The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen 
# numbers is different. 
# 
#  It is guaranteed that the number of unique combinations that sum up to 
# target is less than 150 combinations for the given input. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple 
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#  
# 
#  Example 3: 
# 
#  
# Input: candidates = [2], target = 1
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  All elements of candidates are distinct. 
#  1 <= target <= 500 
#  
#  Related Topics Array Backtracking 👍 8391 👎 195


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = {}

        # sorting helps avoid duplicates
        candidates = sorted(candidates)
        size = len(candidates)

        def rec(local_target, index, solutions):
            # some solution found
            if local_target == 0:
                if solutions:
                    _sum = sum(solutions[0])
                    if _sum not in cache:
                        cache[_sum] = []
                    new_cache = cache[_sum]
                    new_cache.extend(solutions)
                    cache[_sum] = new_cache
                return

            # boundary conditions
            if index < 0 or index >= size or local_target < 0:
                return

            candidate = candidates[index]
            # since the array is sorted, if current element is very high,
            # no more solutions can be found
            if candidate > local_target:
                return

            # include the current element
            new_solutions = [x + [candidate] for x in solutions] if solutions else [[candidate]]
            rec(local_target - candidate, index, new_solutions)
            # exclude the current element
            new_solutions = [] + solutions
            rec(local_target, index + 1, new_solutions)

        rec(target, 0, [])

        return cache.get(target, [])
# leetcode submit region end(Prohibit modification and deletion)
