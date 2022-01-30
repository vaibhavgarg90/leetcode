# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the same 
# tree, construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
#  Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 4051 ?
# ? 69


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        in_order_dict = {}
        for i, val in enumerate(inorder):
            in_order_dict[val] = i

        def rec(post_order_index, in_order_index1, in_order_index2):
            if post_order_index < 0 or post_order_index >= n:
                return None, post_order_index
            if in_order_index1 < 0 or in_order_index1 >= n:
                return None, post_order_index
            if in_order_index2 < 0 or in_order_index2 >= n:
                return None, post_order_index
            root_val = postorder[post_order_index]
            in_order_index = in_order_dict[root_val]
            root = TreeNode(root_val)
            if in_order_index < in_order_index2:
                root.right, post_order_index = rec(post_order_index - 1, in_order_index + 1, in_order_index2)
            if in_order_index > in_order_index1:
                root.left, post_order_index = rec(post_order_index - 1, in_order_index1, in_order_index - 1)
            return root, post_order_index

        return rec(n - 1, 0, n - 1)[0]
# leetcode submit region end(Prohibit modification and deletion)
