# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  A height-balanced binary tree is a binary tree in which the depth of the two 
# subtrees of every node never differs by more than one. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in a strictly increasing order. 
#  
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 5824 👎 341


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def rec(i, j):
            if i > j:
                return None
            mid = (i + j) // 2
            left = rec(i, mid - 1)
            right = rec(mid + 1, j)
            return TreeNode(nums[mid], left, right)

        return rec(0, len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)
