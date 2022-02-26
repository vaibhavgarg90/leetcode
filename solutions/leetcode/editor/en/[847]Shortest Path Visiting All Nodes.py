# # You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
# 
# # You are given an array graph where graph[i] is a list of all the nodes 
# connected 
# # with node i by an edge. 
# # 
# # Return the length of the shortest path that visits every node. You may 
# start 
# # and stop at any node, you may revisit nodes multiple times, and you may 
# reuse 
# # edges. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: graph = [[1,2,3],[0],[0],[0]]
# # Output: 4
# # Explanation: One possible path is [1,0,2,0,3]
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# # Output: 4
# # Explanation: One possible path is [0,1,4,2,3]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # n == graph.length 
# # 1 <= n <= 12 
# # 0 <= graph[i].length < n 
# # graph[i] does not contain i. 
# # If graph[a] contains b, then graph[b] contains a. 
# # The input graph is always connected. 
# # 
# # Related Topics Dynamic Programming Bit Manipulation Breadth-First Search 
# # Graph Bitmask 👍 1559 👎 104
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        level = 0
        visited = set(queue)
        while queue:
            next_queue = []
            for node, mask in queue:
                for neighbor in graph[node]:
                    neighbor_mask = mask | (1 << neighbor)
                    if neighbor_mask == ending_mask:
                        return level + 1
                    neighbor_state = (neighbor, neighbor_mask)
                    if neighbor_state not in visited:
                        visited.add(neighbor_state)
                        next_queue.append(neighbor_state)
            level += 1
            queue = next_queue
# leetcode submit region end(Prohibit modification and deletion)
