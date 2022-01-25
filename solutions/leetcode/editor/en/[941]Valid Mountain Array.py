# Given an array of integers arr, return true if and only if it is a valid 
# mountain array. 
# 
#  Recall that arr is a mountain array if and only if: 
# 
#  
#  arr.length >= 3 
#  There exists some i with 0 < i < arr.length - 1 such that:
#  
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  
#  Example 1: 
#  Input: arr = [2,1]
# Output: false
#  Example 2: 
#  Input: arr = [3,5,5]
# Output: false
#  Example 3: 
#  Input: arr = [0,3,2,1]
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10⁴ 
#  0 <= arr[i] <= 10⁴ 
#  
#  Related Topics Array 👍 1547 👎 124


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        # check strictly increasing
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        # nothing increasing or everything increasing
        if i == 0 or i == n - 1:
            return False
        # check strictly decreasing
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        # found a point without strictly decreasing
        if i < n - 1:
            return False
        # all good
        return True
# leetcode submit region end(Prohibit modification and deletion)
