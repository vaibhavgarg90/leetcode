# Given the root of a binary tree, return all root-to-leaf paths in any order. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: ["1"]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics String Tree Depth-First Search Binary Tree 👍 3574 👎 168


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def rec(root, path):
            if not root.left and not root.right:
                res.append(path)
                return
            if root.left:
                rec(root.left, path + "->" + str(root.left.val))
            if root.right:
                rec(root.right, path + "->" + str(root.right.val))

        rec(root, str(root.val))
        return res
# leetcode submit region end(Prohibit modification and deletion)
