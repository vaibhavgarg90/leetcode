# A string s is called happy if it satisfies the following conditions: 
# 
#  
#  s only contains the letters 'a', 'b', and 'c'. 
#  s does not contain any of "aaa", "bbb", or "ccc" as a substring. 
#  s contains at most a occurrences of the letter 'a'. 
#  s contains at most b occurrences of the letter 'b'. 
#  s contains at most c occurrences of the letter 'c'. 
#  
# 
#  Given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. If there is no 
# such string, return the empty string "". 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#  
# 
#  Example 2: 
# 
#  
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
#  Related Topics String Greedy Heap (Priority Queue) 👍 975 👎 171


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        def heap_insert(count, char):
            heapq.heappush(max_heap, (-1 * count, char))

        def heap_pop():
            next_char_count, next_char = heapq.heappop(max_heap)
            return -1 * next_char_count, next_char

        def get_next_char(prev_char, prev_char_count):
            next_char_count, next_char = heap_pop()
            if next_char_count <= 0:
                return ""
            if next_char != prev_char or prev_char_count < 2:
                heap_insert(next_char_count - 1, next_char)
                return next_char
            tmp_char_count, tmp_char = next_char_count, next_char
            next_char_count, next_char = heap_pop()
            if next_char_count <= 0:
                return ""
            heap_insert(tmp_char_count, tmp_char)
            heap_insert(next_char_count - 1, next_char)
            return next_char

        def build():
            res = ""
            prev_char = ""
            prev_char_count = 0
            while True:
                next_char = get_next_char(prev_char, prev_char_count)
                if not next_char:
                    break
                res += next_char
                if next_char == prev_char:
                    prev_char_count += 1
                else:
                    prev_char_count = 1
                prev_char = next_char
            return res

        heap_insert(a, "a")
        heap_insert(b, "b")
        heap_insert(c, "c")
        return build()
# leetcode submit region end(Prohibit modification and deletion)
