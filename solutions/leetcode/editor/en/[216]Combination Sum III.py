# Find all valid combinations of k numbers that sum up to n such that the 
# following conditions are true: 
# 
#  
#  Only numbers 1 through 9 are used. 
#  Each number is used at most once. 
#  
# 
#  Return a list of all possible valid combinations. The list must not contain 
# the same combination twice, and the combinations may be returned in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations. 
# 
#  Example 2: 
# 
#  
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
#  
# 
#  Example 3: 
# 
#  
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1
# +2+3+4 = 10 and since 10 > 1, there are no valid combination.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= k <= 9 
#  1 <= n <= 60 
#  
#  Related Topics Array Backtracking 👍 2459 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def rec(k, n, start, end, used_set):
            # print(f"{k = }, {n = }, {start = }, {end = }, {used_set = }")
            if k == 0 and n == 0:
                res.append(sorted(used_set))
            for num in range(start, min(n + 1, end + 1)):
                used_set.add(num)
                rec(k - 1, n - num, num + 1, end, used_set)
                used_set.remove(num)

        used_set = {-1}
        used_set.pop()
        rec(k, n, 1, 9, used_set)
        return res
# leetcode submit region end(Prohibit modification and deletion)
