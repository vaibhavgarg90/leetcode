# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree,
#  construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder and inorder consist of unique values. 
#  Each value of inorder also appears in preorder. 
#  preorder is guaranteed to be the preorder traversal of the tree. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  
#  Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 7499 ?
# ? 190


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        in_order_dict = {}
        for i, val in enumerate(inorder):
            in_order_dict[val] = i

        def rec(pre_order_index, in_order_index1, in_order_index2):
            if pre_order_index < 0 or pre_order_index >= n:
                return None, pre_order_index
            if in_order_index1 < 0 or in_order_index1 >= n:
                return None, pre_order_index
            if in_order_index2 < 0 or in_order_index2 >= n:
                return None, pre_order_index
            root_val = preorder[pre_order_index]
            in_order_index = in_order_dict[root_val]
            root = TreeNode(root_val)
            if in_order_index > in_order_index1:
                root.left, pre_order_index = rec(pre_order_index + 1, in_order_index1, in_order_index - 1)
            if in_order_index < in_order_index2:
                root.right, pre_order_index = rec(pre_order_index + 1, in_order_index + 1, in_order_index2)
            return root, pre_order_index

        return rec(0, 0, n - 1)[0]
# leetcode submit region end(Prohibit modification and deletion)
