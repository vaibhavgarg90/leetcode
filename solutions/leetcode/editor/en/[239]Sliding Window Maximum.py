# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 8275 👎 287


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = []

        # q stores indices so that elements outside the sliding window can be identified and removed
        # indices are always present in the ascending order in the q
        # the elements at the indices in the q are guaranteed to be in the descending order
        # not all indices are added, only the relevant ones which might impact the output are added
        def check_and_enqueue(index, min_index):
            if not q:
                q.append(index)
                return

            # remove indices outside the sliding window
            if q[0] < min_index:
                q.remove(q[0])

            # ensure that the descending order is maintained
            num = nums[index]
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(index)

        # append first set of elements to the q
        for i in range(k):
            check_and_enqueue(i, 0)

        # pick up first element from the q for each sliding window
        for i in range(k, n):
            res.append(nums[q[0]])
            check_and_enqueue(i, i - k + 1)

        # process the last sliding window
        res.append(nums[q[0]])

        return res
# leetcode submit region end(Prohibit modification and deletion)
