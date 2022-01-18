# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots. 
# 
#  Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return if n new flowers can be planted 
# in the flowerbed without violating the no-adjacent-flowers rule. 
# 
#  
#  Example 1: 
#  Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#  Example 2: 
#  Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= flowerbed.length <= 2 * 10⁴ 
#  flowerbed[i] is 0 or 1. 
#  There are no two adjacent flowers in flowerbed. 
#  0 <= n <= flowerbed.length 
#  
#  Related Topics Array Greedy 👍 2244 👎 573


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        _size = len(flowerbed)
        if n == 0:
            return True
        if _size == 1:
            return flowerbed[0] == 0

        spaces_available = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            spaces_available += 1
            flowerbed[0] = 1

        for i in range(1, _size - 1):
            status = flowerbed[i]
            if status == 1:
                continue
            _prev = flowerbed[i - 1]
            _next = flowerbed[i + 1]
            if _prev == 0 and _next == 0:
                spaces_available += 1
                flowerbed[i] = 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            spaces_available += 1
            flowerbed[-1] = 1

        return spaces_available >= n
# leetcode submit region end(Prohibit modification and deletion)
