# The count-and-say sequence is a sequence of digit strings defined by the 
# recursive formula: 
# 
#  
#  countAndSay(1) = "1" 
#  countAndSay(n) is the way you would "say" the digit string from countAndSay(
# n-1), which is then converted into a different digit string. 
#  
# 
#  To determine how you "say" a digit string, split it into the minimal number 
# of groups so that each group is a contiguous section all of the same character. 
# Then for each group, say the number of characters, then say the character. To 
# convert the saying into a digit string, replace the counts with a number and 
# concatenate every saying. 
# 
#  For example, the saying and conversion for digit string "3322251": 
# 
#  Given a positive integer n, return the nᵗʰ term of the count-and-say 
# sequence. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 30 
#  
#  Related Topics String 👍 1048 👎 2903


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countAndSay(self, n: int) -> str:
        next = {}
        cur_str = "1"

        def update_count(split, count, digit_str):
            count_str = str(count)
            split.append(count_str)
            split.append(digit_str)
            next[digit_str * count] = count_str + digit_str

        for _ in range(1, n):
            count = 0
            prev_digit_str = ""
            split: List[str] = []
            for i, c in enumerate(cur_str):
                if c == prev_digit_str:
                    count += 1
                else:
                    if count:
                        update_count(split, count, prev_digit_str)
                    rem_str = cur_str[i:]
                    if rem_str in next:
                        split.append(next[rem_str])
                        count = 0
                        break
                    prev_digit_str = c
                    count = 1
            if count:
                update_count(split, count, prev_digit_str)
            next_str = "".join(split)
            next[cur_str] = next_str
            cur_str = next_str

        return cur_str
# leetcode submit region end(Prohibit modification and deletion)
