# Let's call an array arr a mountain if the following properties hold: 
# 
#  
#  arr.length >= 3 
#  There exists some i with 0 < i < arr.length - 1 such that:
#  
#  arr[0] < arr[1] < ... arr[i-1] < arr[i] 
#  arr[i] > arr[i+1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  Given an integer array arr that is guaranteed to be a mountain, return any i 
# such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[
# arr.length - 1]. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [0,1,0]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [0,2,1,0]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [0,10,5,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= arr.length <= 10⁴ 
#  0 <= arr[i] <= 10⁶ 
#  arr is guaranteed to be a mountain array. 
#  
# 
#  
# Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) 
# solution? Related Topics Array Binary Search 👍 1960 👎 1554


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n: int = len(arr)
        if n == 3:
            return 1

        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low += 1
                continue
            if mid == n - 1:
                high -= 1
                continue
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1
# leetcode submit region end(Prohibit modification and deletion)
