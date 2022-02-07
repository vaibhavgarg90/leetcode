# Given the root of a binary tree, return the length of the diameter of the 
# tree. 
# 
#  The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree. This path may or may not pass through the root. 
# 
#  The length of a path between two nodes is represented by the number of edges 
# between them. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 7030 👎 433


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def rec(node):
            if not node:
                return 0, 0
            left_diameter, left_nodes = rec(node.left)
            right_diameter, right_nodes = rec(node.right)
            max_diameter = max(max(left_diameter, right_diameter), left_nodes + right_nodes)
            return max_diameter, 1 + max(left_nodes, right_nodes)

        return rec(root)[0]
# leetcode submit region end(Prohibit modification and deletion)
