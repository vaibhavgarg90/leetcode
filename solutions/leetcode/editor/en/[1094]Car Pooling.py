# There is a car with capacity empty seats. The vehicle only drives east (i.e., 
# it cannot turn around and drive west). 
# 
#  You are given the integer capacity and an array trips where trip[i] = [
# numPassengersi, fromi, toi] indicates that the iᵗʰ trip has numPassengersi passengers 
# and the locations to pick them up and drop them off are fromi and toi 
# respectively. The locations are given as the number of kilometers due east from the car's 
# initial location. 
# 
#  Return true if it is possible to pick up and drop off all passengers for all 
# the given trips, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
#  
# 
#  Example 2: 
# 
#  
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= trips.length <= 1000 
#  trips[i].length == 3 
#  1 <= numPassengersi <= 100 
#  0 <= fromi < toi <= 1000 
#  1 <= capacity <= 10⁵ 
#  
#  Related Topics Array Sorting Heap (Priority Queue) Simulation Prefix Sum 👍 2
# 246 👎 57


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        # sort the trips based on pick-up location
        trips = sorted(trips, key=lambda x: x[1])
        # index of the next trip that needs to be taken up
        # all the trips before this index have been served
        trips_handled = 0
        # q of all the running trips
        running_trips = []
        # initialize remaining capacity
        remaining_capacity = capacity
        for i in range(1001):
            if trips_handled == n:
                return True
            # remove all the `running_trips` that are ending at this point
            for trip_index in running_trips[:]:
                running_trip = trips[trip_index]
                end_location = running_trip[2]
                if end_location == i:
                    running_trips.remove(trip_index)
                    remaining_capacity += running_trip[0]
            # add all the trips to `running_trips` that are starting at this point
            while trips_handled < n and trips[trips_handled][1] == i:
                num_people = trips[trips_handled][0]
                if num_people > remaining_capacity:
                    return False
                running_trips.append(trips_handled)
                remaining_capacity -= num_people
                trips_handled += 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
