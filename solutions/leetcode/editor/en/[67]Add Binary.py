#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        res_len = 1 + max(len_a, len_b)
        res_str_list = ["0"] * res_len

        a_i = len_a - 1
        b_i = len_b - 1
        res_i = res_len - 1
        carry = 0
        while res_i >= 0:
            cur_a = 0
            cur_b = 0
            if a_i >= 0:
                cur_a = int(a[a_i])
                a_i -= 1
            if b_i >= 0:
                cur_b = int(b[b_i])
                b_i -= 1

            cur_res = cur_a + cur_b + carry
            cur_res_digit = cur_res % 2
            carry = cur_res // 2

            res_str_list[res_i] = str(cur_res_digit)
            res_i -= 1

        found = False
        res = ""
        i = 0
        while i < res_len:
            cur_res_digit = res_str_list[i]
            if not found and cur_res_digit == "1":
                found = True
            if found:
                res += cur_res_digit

            i += 1

        return res or "0"


# @lc code=end

