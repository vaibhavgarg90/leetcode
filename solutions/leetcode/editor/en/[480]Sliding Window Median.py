# The median is the middle value in an ordered integer list. If the size of the 
# list is even, there is no middle value. So the median is the mean of the two 
# middle values. 
# 
#  
#  For examples, if arr = [2,3,4], the median is 3. 
#  For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5. 
#  
# 
#  You are given an integer array nums and an integer k. There is a sliding 
# window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window 
# moves right by one position. 
# 
#  Return the median array for each window in the original array. Answers 
# within 10⁻⁵ of the actual value will be accepted. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation: 
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
#  Related Topics Array Hash Table Sliding Window Heap (Priority Queue) 👍 1983 
# 👎 124


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return [float(num) for num in nums]

        n = len(nums)
        min_heap, max_heap = [], []

        def rebalance():
            min_heap_len = len(min_heap)
            max_heap_len = len(max_heap)
            if min_heap_len in (max_heap_len, 1 + max_heap_len):
                return
            while len(min_heap) < len(max_heap):
                heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
            while len(min_heap) - len(max_heap) > 1:
                heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

        def get_heap_and_num(num):
            min_heap_top = min_heap[0]
            heap = max_heap if num < min_heap_top else min_heap
            num = -1 * num if num < min_heap_top else num
            return heap, num

        def insert(num):
            heap, num = get_heap_and_num(num)
            heapq.heappush(heap, num)

        def remove(num):
            heap, num = get_heap_and_num(num)
            heap.remove(num)
            heapq.heapify(heap)

        def get_median():
            if len(min_heap) > len(max_heap):
                return min_heap[0]
            return (min_heap[0] + (-1 * max_heap[0])) / 2

        initial_k_nums_sorted = sorted(nums[:k])
        res = []
        i = 0
        while i < k // 2:
            num = initial_k_nums_sorted[i]
            heapq.heappush(max_heap, -1 * num)
            i += 1
        while i < k:
            num = initial_k_nums_sorted[i]
            heapq.heappush(min_heap, num)
            i += 1
        while i < n:
            # print(f"{i = }, {nums[i - k] = }, {nums[i] = }, {min_heap = }, {max_heap = }")
            res.append(get_median())
            insert(nums[i])
            remove(nums[i - k])
            rebalance()
            i += 1
        res.append(get_median())
        return res
# leetcode submit region end(Prohibit modification and deletion)
