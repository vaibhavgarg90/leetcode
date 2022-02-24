# You are given a large integer represented as an integer array digits, where 
# each digits[i] is the iᵗʰ digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. The large integer does 
# not contain any leading 0's. 
# 
#  Increment the large integer by one and return the resulting array of digits. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#  
# 
#  Example 2: 
# 
#  
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#  
# 
#  Example 3: 
# 
#  
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  digits does not contain any leading 0's. 
#  
#  Related Topics Array Math 👍 3713 👎 3971


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = [1] * (n + 1)
        carry = 1
        for i in range(n - 1, -1, -1):
            _sum = digits[i] + carry
            res[i + 1] = _sum % 10
            carry = _sum // 10
        if not carry:
            res.pop(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
