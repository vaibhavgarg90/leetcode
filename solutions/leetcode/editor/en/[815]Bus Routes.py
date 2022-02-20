# You are given an array routes representing bus routes where routes[i] is a 
# bus route that the iᵗʰ bus repeats forever. 
# 
#  
#  For example, if routes[0] = [1, 5, 7], this means that the 0ᵗʰ bus travels 
# in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever. 
#  
# 
#  You will start at the bus stop source (You are not on any bus initially), 
# and you want to go to the bus stop target. You can travel between bus stops by 
# buses only. 
# 
#  Return the least number of buses you must take to travel from source to 
# target. Return -1 if it is not possible. 
# 
#  
#  Example 1: 
# 
#  
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then 
# take the second bus to the bus stop 6.
#  
# 
#  Example 2: 
# 
#  
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target =
#  12
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= routes.length <= 500. 
#  1 <= routes[i].length <= 10⁵ 
#  All the values of routes[i] are unique. 
#  sum(routes[i].length) <= 10⁵ 
#  0 <= routes[i][j] < 10⁶ 
#  0 <= source, target < 10⁶ 
#  
#  Related Topics Array Hash Table Breadth-First Search 👍 1797 👎 46


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_routes_dict = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_routes_dict[stop].add(i)

        num_stops = 1
        visited = set()
        q = stop_routes_dict[source]
        while q:
            next_q = set()
            for route in q:
                if route in visited:
                    continue
                for stop in routes[route]:
                    if stop == target:
                        return num_stops
                    next_q.update(stop_routes_dict[stop])
                visited.add(route)
            num_stops += 1
            q = next_q
        return -1
# leetcode submit region end(Prohibit modification and deletion)
