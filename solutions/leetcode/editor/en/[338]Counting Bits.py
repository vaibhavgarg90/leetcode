# Given an integer n, return an array ans of length n + 1 such that for each i (
# 0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 10⁵ 
#  
# 
#  
#  Follow up: 
# 
#  
#  It is very easy to come up with a solution with a runtime of O(n log n). Can 
# you do it in linear time O(n) and possibly in a single pass? 
#  Can you do it without using any built-in function (i.e., like __builtin_
# popcount in C++)? 
#  
#  Related Topics Dynamic Programming Bit Manipulation 👍 5301 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1, 1]
        if n < 3:
            return res[0: n + 1]
        cur_power_of_2 = 2
        next_power_of_2 = cur_power_of_2 << 1
        for num in range(3, n + 1):
            if num == next_power_of_2:
                res.append(1)
                cur_power_of_2 = next_power_of_2
                next_power_of_2 = next_power_of_2 << 1
            else:
                res.append(1 + res[num - cur_power_of_2])
        return res
# leetcode submit region end(Prohibit modification and deletion)
