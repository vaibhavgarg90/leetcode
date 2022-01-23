# Given the root of a binary tree, invert the tree, and return its root. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,3]
# Output: [2,3,1]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 74
# 05 👎 101


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        l_inverted = self.invertTree(root.left)
        r_inverted = self.invertTree(root.right)
        root.left = r_inverted
        root.right = l_inverted
        return root
# leetcode submit region end(Prohibit modification and deletion)
