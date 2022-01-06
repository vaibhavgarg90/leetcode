# You have k lists of sorted integers in non-decreasing order. Find the 
# smallest range that includes at least one number from each of the k lists. 
# 
#  We define the range [a, b] is smaller than range [c, d] if b - a < d - c or 
# a < c if b - a == d - c. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  nums.length == k 
#  1 <= k <= 3500 
#  1 <= nums[i].length <= 50 
#  -10⁵ <= nums[i][j] <= 10⁵ 
#  nums[i] is sorted in non-decreasing order. 
#  
#  Related Topics Array Hash Table Greedy Sliding Window Sorting Heap (Priority 
# Queue) 👍 1874 👎 32


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        _range = [-10 ** 5 - 1, 10 ** 5 + 1]
        _max = -10 ** 5 - 1
        # add first element of all the k lists into the heap
        for l_index, l in enumerate(nums):
            elem = l[0]
            _max = max(_max, elem)
            heap.append((l[0], l_index, 0))
        # heapify
        heapq.heapify(heap)
        # repeat till one of the lists gets exhausted
        while True:
            # get the min from the heap
            _min, l_index, e_index = heapq.heappop(heap)
            # check if the current range is smaller than the previous min range
            if _max - _min < _range[1] - _range[0]:
                _range = [_min, _max]
                # just for the sake of run-time optimization
                if _min == _max:
                    break
            # check if the list is exhausted
            if e_index == len(nums[l_index]) - 1:
                break
            # add the next element from the list to the heap
            e_index += 1
            elem = nums[l_index][e_index]
            _max = max(_max, elem)
            heapq.heappush(heap, (elem, l_index, e_index))
        return _range
# leetcode submit region end(Prohibit modification and deletion)
