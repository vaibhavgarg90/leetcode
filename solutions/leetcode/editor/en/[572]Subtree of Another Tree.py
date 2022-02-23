# Given the roots of two binary trees root and subRoot, return true if there is 
# a subtree of root with the same structure and node values of subRoot and false 
# otherwise. 
# 
#  A subtree of a binary tree tree is a tree that consists of a node in tree 
# and all of this node's descendants. The tree tree could also be considered as a 
# subtree of itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the root tree is in the range [1, 2000]. 
#  The number of nodes in the subRoot tree is in the range [1, 1000]. 
#  -10⁴ <= root.val <= 10⁴ 
#  -10⁴ <= subRoot.val <= 10⁴ 
#  
#  Related Topics Tree Depth-First Search String Matching Binary Tree Hash 
# Function 👍 4822 👎 246


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_equal(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and is_equal(root1.left, root2.left) and is_equal(root1.right, root2.right)

        def rec(root1, root2):
            if not root1:
                return False
            if is_equal(root1, root2):
                return True
            return rec(root1.left, root2) or rec(root1.right, root2)

        return rec(root, subRoot)
# leetcode submit region end(Prohibit modification and deletion)
