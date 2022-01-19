# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the 
# node's key. 
#  The right subtree of a node contains only nodes with keys greater than the 
# node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 8499
#  👎 820


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        _min = -2 ** 32
        _max = 2 ** 32
        
        def rec(root, _min, _max):
            if not _min <= root.val <= _max:
                return False
            if not root.left and not root.right:
                return True
            is_left_valid_bst = True
            is_right_valid_bst = True
            if root.left:
                if root.left.val >= root.val:
                    return False
                is_left_valid_bst = rec(root.left, _min, root.val - 1)
            if root.right:
                if root.right.val <= root.val:
                    return False
                is_right_valid_bst = rec(root.right, root.val + 1, _max)
            return is_left_valid_bst and is_right_valid_bst
        
        return rec(root, _min, _max)
# leetcode submit region end(Prohibit modification and deletion)
