# Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
# and M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, 2 is written as II in Roman numeral, just two one's added 
# together. 12 is written as XII, which is simply X + II. The number 27 is written as 
# XXVII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same 
# principle applies to the number nine, which is written as IX. There are six 
# instances where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given an integer, convert it to a roman numeral. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#  
# 
#  Example 3: 
# 
#  
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 3999 
#  
#  Related Topics Hash Table Math String 👍 2564 👎 3682


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX"
        }
        roman = ""
        # 1000
        s, num = self.roman_util(num, "M", 1000, True)
        roman += s
        # 900
        s, num = self.roman_util(num, "CM", 900)
        roman += s
        # 500
        s, num = self.roman_util(num, "D", 500)
        roman += s
        # 400
        s, num = self.roman_util(num, "CD", 400)
        roman += s
        # 100
        s, num = self.roman_util(num, "C", 100, True)
        roman += s
        # 90
        s, num = self.roman_util(num, "XC", 90)
        roman += s
        # 50
        s, num = self.roman_util(num, "L", 50)
        roman += s
        # 40
        s, num = self.roman_util(num, "XL", 40)
        roman += s
        # 10
        s, num = self.roman_util(num, "X", 10, True)
        roman += s
        # 1-9
        roman += d.get(num)
        return roman

    def roman_util(self, num, lit, val, multi=False):
        if num < val:
            return "", num
        roman = ""
        count = int(num / val) if multi else 1
        for _ in range(count):
            roman += lit
        num %= val
        return roman, num
# leetcode submit region end(Prohibit modification and deletion)
