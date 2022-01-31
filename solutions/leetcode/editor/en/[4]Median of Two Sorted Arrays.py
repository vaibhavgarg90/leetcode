# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays. 
# 
#  The overall run time complexity should be O(log (m+n)). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
#  Related Topics Array Binary Search Divide and Conquer 👍 14636 👎 1843


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            smaller, bigger = nums1, nums2
        else:
            smaller, bigger = nums2, nums1
        total = len(smaller) + len(bigger)
        half = total // 2
        left, right = 0, len(smaller) - 1
        while True:
            i = (left + right) // 2  # index in smaller
            j = half - i - 2  # index in bigger
            smaller_left = smaller[i] if i >= 0 else float("-infinity")
            smaller_right = smaller[i + 1] if (i + 1) < len(smaller) else float("infinity")
            bigger_left = bigger[j] if j >= 0 else float("-infinity")
            bigger_right = bigger[j + 1] if (j + 1) < len(bigger) else float("infinity")
            if smaller_left <= bigger_right and bigger_left <= smaller_right:
                # even:
                if total % 2 == 0:
                    return (max(smaller_left, bigger_left) + min(smaller_right, bigger_right)) / 2
                # odd:
                return min(smaller_right, bigger_right)
            elif smaller_left > bigger_right:
                right = i - 1
            else:
                left = i + 1
# leetcode submit region end(Prohibit modification and deletion)
