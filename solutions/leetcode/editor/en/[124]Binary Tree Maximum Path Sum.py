# A path in a binary tree is a sequence of nodes where each pair of adjacent 
# nodes in the sequence has an edge connecting them. A node can only appear in the 
# sequence at most once. Note that the path does not need to pass through the root. 
# 
# 
#  The path sum of a path is the sum of the node's values in the path. 
# 
#  Given the root of a binary tree, return the maximum path sum of any non-
# empty path. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 
# = 42.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Dynamic Programming Tree Depth-First Search Binary Tree 👍 860
# 7 👎 510


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def rec(root):
            if not root.left and not root.right:
                return root.val, root.val
            l_max_seen_so_far, l_max_contribution = None, None
            r_max_seen_so_far, r_max_contribution = None, None
            if root.left:
                l_max_seen_so_far, l_max_contribution = rec(root.left)
            if root.right:
                r_max_seen_so_far, r_max_contribution = rec(root.right)
            if l_max_seen_so_far is not None and r_max_seen_so_far is not None:
                max_seen_so_far = max(l_max_seen_so_far, r_max_seen_so_far)
                max_seen_so_far = max(max_seen_so_far, root.val + l_max_contribution)
                max_seen_so_far = max(max_seen_so_far, root.val + r_max_contribution)
                max_seen_so_far = max(max_seen_so_far, root.val + l_max_contribution + r_max_contribution)
                max_contribution = root.val + max(l_max_contribution, r_max_contribution)
            elif l_max_seen_so_far is not None:
                max_seen_so_far = max(l_max_seen_so_far, root.val + l_max_contribution)
                max_contribution = root.val + l_max_contribution
            elif r_max_seen_so_far is not None:
                max_seen_so_far = max(r_max_seen_so_far, root.val + r_max_contribution)
                max_contribution = root.val + r_max_contribution
            max_seen_so_far = max(max_seen_so_far, root.val)
            max_contribution = max(max_contribution, root.val)
            return max_seen_so_far, max_contribution

        return rec(root)[0]
# leetcode submit region end(Prohibit modification and deletion)
