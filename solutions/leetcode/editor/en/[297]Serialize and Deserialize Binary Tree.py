# Serialization is the process of converting a data structure or object into a 
# sequence of bits so that it can be stored in a file or memory buffer, or 
# transmitted across a network connection link to be reconstructed later in the same or 
# another computer environment. 
# 
#  Design an algorithm to serialize and deserialize a binary tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. You 
# just need to ensure that a binary tree can be serialized to a string and this 
# string can be deserialized to the original tree structure. 
# 
#  Clarification: The input/output format is the same as how LeetCode 
# serializes a binary tree. You do not necessarily need to follow this format, so please be 
# creative and come up with different approaches yourself. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#  
# 
#  Example 2: 
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
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics String Tree Depth-First Search Breadth-First Search Design 
# Binary Tree 👍 5923 👎 233


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            json.dumps([])
        lst = []
        q = [root]
        while q:
            q2 = []
            while q:
                node = q.pop(0)
                node_val = node.val if node else None
                lst.append(node_val)
                if not node:
                    continue
                q2.append(node.left)
                q2.append(node.right)
            q = q2
        return json.dumps(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        lst = json.loads(data)
        if not lst:
            return None
        root = TreeNode(lst[0]) if lst[0] is not None else None
        n = len(lst)
        i = 1
        q = [root]
        while q and i < n:
            q2 = []
            while q and i < n:
                node = q.pop(0)
                left = lst[i] if i < n else None
                right = lst[i + 1] if (i + 1) < n else None
                if left is not None:
                    node.left = TreeNode(left)
                    q2.append(node.left)
                if right is not None:
                    node.right = TreeNode(right)
                    q2.append(node.right)
                i += 2
            q = q2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
