# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant 
# of itself according to the LCA definition.
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁵]. 
#  -10⁹ <= Node.val <= 10⁹ 
#  All Node.val are unique. 
#  p != q 
#  p and q will exist in the tree. 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 8532 👎 251


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def rec(root):
            if not root:
                return False, None
            left_found, left_lca = rec(root.left)
            right_found, right_lca = rec(root.right)
            if left_lca or right_lca:
                return True, left_lca or right_lca
            if (left_found or right_found) and root in (p, q):
                return True, root
            if left_found and right_found:
                return True, root
            if root in (p, q):
                return True, None
            return left_found or right_found, None

        return rec(root)[1]
# leetcode submit region end(Prohibit modification and deletion)
