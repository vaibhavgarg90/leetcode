# Given the root of a binary tree, return the average value of the nodes on 
# each level in the form of an array. Answers within 10⁻⁵ of the actual answer will 
# be accepted.
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, 
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 27
# 21 👎 224


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while q:
            children = []
            _sum = 0
            n = len(q)
            while q:
                node = q.pop()
                _sum += node.val
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(_sum/n)
            q = children
        return res
# leetcode submit region end(Prohibit modification and deletion)
