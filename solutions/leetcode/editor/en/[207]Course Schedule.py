# There are a total of numCourses courses you have to take, labeled from 0 to 
# numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai,
#  bi] indicates that you must take course bi first if you want to take course ai.
#  
# 
#  
#  For example, the pair [0, 1], indicates that to take course 0 you have to 
# first take course 1. 
#  
# 
#  Return true if you can finish all courses. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you 
# should also have finished course 1. So it is impossible.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= numCourses <= 10⁵ 
#  0 <= prerequisites.length <= 5000 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  All the pairs prerequisites[i] are unique. 
#  
#  Related Topics Depth-First Search Breadth-First Search Graph Topological 
# Sort 👍 8580 👎 338


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def memoization(f):
            dp = {}

            def inner(course, cur_prerequisites, course_prerequisites):
                if course not in dp:
                    dp[course] = f(course, cur_prerequisites, course_prerequisites)
                return dp[course]

            return inner

        @memoization
        def dfs(course, cur_prerequisites, course_prerequisites):
            if course in cur_prerequisites:
                return False
            if course not in course_prerequisites:
                return True
            cur_prerequisites.add(course)
            for p in course_prerequisites[course]:
                if not dfs(p, cur_prerequisites, course_prerequisites):
                    return False
            cur_prerequisites.remove(course)
            return True

        course_prerequisites = {}
        for course, prerequisite in prerequisites:
            cur_course_prerequisites = course_prerequisites.get(course, set())
            cur_course_prerequisites.add(prerequisite)
            course_prerequisites[course] = cur_course_prerequisites

        for i in range(numCourses):
            if not dfs(i, set(), course_prerequisites):
                return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
