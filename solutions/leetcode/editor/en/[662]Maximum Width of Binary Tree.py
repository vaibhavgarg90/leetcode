# Given the root of a binary tree, return the maximum width of the given tree. 
# 
#  The maximum width of a tree is the maximum width among all levels. 
# 
#  The width of one level is defined as the length between the end-nodes (the 
# leftmost and rightmost non-null nodes), where the null nodes between the end-
# nodes are also counted into the length calculation. 
# 
#  It is guaranteed that the answer will in the range of 32-bit signed integer. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (
# 5,3,null,9).
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,3,null,5,3]
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (
# 5,3).
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 
# (3,2).
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3000]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 32
# 44 👎 514


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q = [(root, 0)]
        while q:
            children = []
            start = q[0][1]
            for node, _id in q:
                if node.left:
                    children.append((node.left, _id * 2))
                if node.right:
                    children.append((node.right, _id * 2 + 1))
            max_width = max(max_width, _id - start + 1)
            q = children
        return max_width
# leetcode submit region end(Prohibit modification and deletion)
