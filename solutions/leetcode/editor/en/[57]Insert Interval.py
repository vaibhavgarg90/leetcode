# You are given an array of non-overlapping intervals intervals where intervals[
# i] = [starti, endi] represent the start and the end of the iᵗʰ interval and 
# intervals is sorted in ascending order by starti. You are also given an interval 
# newInterval = [start, end] that represents the start and end of another interval. 
# 
#  Insert newInterval into intervals such that intervals is still sorted in 
# ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary). 
# 
#  Return intervals after the insertion. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁵ 
#  intervals is sorted by starti in ascending order. 
#  newInterval.length == 2 
#  0 <= start <= end <= 10⁵ 
#  
#  Related Topics Array 👍 4233 👎 315


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        merged_intervals = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged_intervals.append(newInterval)
        while i < n:
            merged_intervals.append(intervals[i])
            i += 1
        return merged_intervals
# leetcode submit region end(Prohibit modification and deletion)
