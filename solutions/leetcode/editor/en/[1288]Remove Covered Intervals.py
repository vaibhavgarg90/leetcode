# Given an array intervals where intervals[i] = [li, ri] represent the interval 
# [li, ri), remove all intervals that are covered by another interval in the list.
#  
# 
#  The interval [a, b) is covered by the interval [c, d) if and only if c <= a 
# and b <= d. 
# 
#  Return the number of remaining intervals. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[2,3]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 1000 
#  intervals[i].length == 2 
#  0 <= li <= ri <= 10⁵ 
#  All the given intervals are unique. 
#  
#  Related Topics Array Sorting 👍 1335 👎 36


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 1

        intervals = sorted(intervals)
        num_intervals = 1
        last_interval = intervals[0]

        def is_covered(first_interval, second_interval):
            return first_interval[0] >= second_interval[0] and first_interval[1] <= second_interval[1]

        for i in range(1, n):
            interval = intervals[i]
            if is_covered(interval, last_interval):
                continue
            elif is_covered(last_interval, interval):
                last_interval = interval
                continue
            last_interval = interval
            num_intervals += 1

        return num_intervals
# leetcode submit region end(Prohibit modification and deletion)
