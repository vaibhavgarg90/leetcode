# Given an integer array nums and two integers lower and upper, return the 
# number of range sums that lie in [lower, upper] inclusive. 
# 
#  Range sum S(i, j) is defined as the sum of the elements in nums between 
# indices i and j inclusive, where i <= j. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their 
# respective sums are: -2, -1, 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  -10⁵ <= lower <= upper <= 10⁵ 
#  The answer is guaranteed to fit in a 32-bit integer. 
#  
#  Related Topics Array Binary Search Divide and Conquer Binary Indexed Tree 
# Segment Tree Merge Sort Ordered Set 👍 1425 👎 154


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]

        def merge_sort(start, end):
            if start == end:
                return 0
            count = 0
            mid = (start + end) // 2
            count += merge_sort(start, mid)
            count += merge_sort(mid + 1, end)
            i = start
            j = k = mid + 1
            while i <= mid:
                while j <= end and sums[j] - sums[i] < lower:
                    j += 1
                while k <= end and sums[k] - sums[i] <= upper:
                    k += 1
                count += k - j
                i += 1
            merge(start, mid, end)
            return count

        def merge(start, mid, end):
            merged_list = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if sums[i] <= sums[j]:
                    merged_list.append(sums[i])
                    i += 1
                else:
                    merged_list.append(sums[j])
                    j += 1
            while i <= mid:
                merged_list.append(sums[i])
                i += 1
            while j <= end:
                merged_list.append(sums[j])
                j += 1
            sums[start: end + 1] = merged_list

        return merge_sort(0, n)
# leetcode submit region end(Prohibit modification and deletion)
