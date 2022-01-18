# Given a characters array letters that is sorted in non-decreasing order and a 
# character target, return the smallest character in the array that is larger 
# than target. 
# 
#  Note that the letters wrap around. 
# 
#  
#  For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#  
# 
#  Example 2: 
# 
#  
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#  
# 
#  Example 3: 
# 
#  
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= letters.length <= 10⁴ 
#  letters[i] is a lowercase English letter. 
#  letters is sorted in non-decreasing order. 
#  letters contains at least two different characters. 
#  target is a lowercase English letter. 
#  
#  Related Topics Array Binary Search 👍 1233 👎 1167


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_greater = letters[0]
        target_int = ord(target)

        low: int = 0
        high: int = len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_int = ord(letters[mid])
            next_greater_int = ord(next_greater)

            # print(f"{low = }, {high = }, {mid = }, {mid_int = }, {next_greater_int =}, {target_int = }")

            if mid_int > target_int:
                prev_diff = next_greater_int - target_int
                curr_diff = mid_int - target_int
                if prev_diff <= 0 or curr_diff < prev_diff:
                    next_greater = letters[mid]
                high = mid - 1
            else:
                low = mid + 1

        return next_greater
# leetcode submit region end(Prohibit modification and deletion)
