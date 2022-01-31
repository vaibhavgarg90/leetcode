# Given two non-negative integers num1 and num2 represented as strings, return 
# the product of num1 and num2, also represented as a string. 
# 
#  Note: You must not use any built-in BigInteger library or convert the inputs 
# to integer directly. 
# 
#  
#  Example 1: 
#  Input: num1 = "2", num2 = "3"
# Output: "6"
#  Example 2: 
#  Input: num1 = "123", num2 = "456"
# Output: "56088"
#  
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 and num2 consist of digits only. 
#  Both num1 and num2 do not contain any leading zero, except the number 0 
# itself. 
#  
#  Related Topics Math String Simulation 👍 3922 👎 1562


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = ""
        m = len(num1)
        n = len(num2)
        carry_over = 0
        for i in range(n):
            local_res = ""
            for _ in range(i):
                local_res += "0"
            # multiply
            for j in range(m):
                v1 = int(num1[m - j - 1])
                v2 = int(num2[n - i - 1])
                multiply = v1 * v2 + carry_over
                local_res = str(multiply % 10) + local_res
                carry_over = int(multiply / 10)
            # if carry over is remaining at the last
            if carry_over:
                local_res = str(carry_over) + local_res
                carry_over = 0
            res2 = ""
            if res:
                m1 = len(local_res)
                n1 = len(res)
                x, y = m1 - 1, n1 - 1
                while x >= 0 or y >= 0:
                    v1 = int(local_res[x]) if x >= 0 else 0
                    v2 = int(res[y]) if y >= 0 else 0
                    _sum = v1 + v2 + carry_over
                    res2 = str(_sum % 10) + res2
                    carry_over = int(_sum / 10)
                    x -= 1
                    y -= 1
                if carry_over:
                    res2 = str(carry_over) + res2
                    carry_over = 0
            else:
                res2 = local_res
            res = res2
        return res
# leetcode submit region end(Prohibit modification and deletion)
