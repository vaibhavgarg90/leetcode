# Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
#  where 0 <= i <= j < n. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁵ 
#  0 <= nums[i] <= 2³¹ - 1 
#  
#  Related Topics Array Hash Table Bit Manipulation Trie 👍 2738 👎 245


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        k = 32
        # create trie
        for binary_num in [f"{x:b}".zfill(k) for x in nums]:
            node = trie
            for binary_digit in binary_num:
                node = node.setdefault(binary_digit, {})
        max_xor = 0
        # loop over all the numbers and maximise the xor value
        for num in nums:
            cur_max_xor_str = ''
            node = trie
            for binary_digit in f"{num:b}".zfill(k):
                tmp = '0' if binary_digit == '1' else '1'
                tmp = tmp if tmp in node else binary_digit
                cur_max_xor_str += tmp
                node = node[tmp]
            cur_max_xor = num ^ int(cur_max_xor_str, 2)
            max_xor = max(max_xor, cur_max_xor)
        return max_xor
# leetcode submit region end(Prohibit modification and deletion)
