# Given two integers n and k, return all possible combinations of k numbers out 
# of the range [1, n]. 
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, k = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics Array Backtracking 👍 3456 👎 117


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def append(num, next_combinations):
            cur_combinations = []
            for combination in next_combinations:
                cur_combination = combination[::]
                cur_combination.append(num)
                cur_combinations.append(cur_combination)
            return cur_combinations

        def rec(n, k):
            if k == n:
                return [[i for i in range(1, n + 1)]]
            if k == 1:
                return [[i] for i in range(1, n + 1)]

            combinations = []
            while n >= k:
                combinations.extend(append(n, rec(n - 1, k - 1)))
                n -= 1
            return combinations

        return rec(n, k)
# leetcode submit region end(Prohibit modification and deletion)
