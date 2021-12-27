# Given a linked list, swap every two adjacent nodes and return its head. You 
# must solve the problem without modifying the values in the list's nodes (i.e., 
# only nodes themselves may be changed.) 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
#  Related Topics Linked List Recursion 👍 5209 👎 260


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = ptr = ListNode()
        slow = head
        fast = head.next
        while fast:
            slow_next = fast.next
            fast_next = slow_next.next if slow_next else None
            ptr.next = fast
            ptr = ptr.next
            ptr.next = slow
            ptr = ptr.next
            ptr.next = None
            slow = slow_next
            fast = fast_next
        if slow:
            ptr.next = slow
            ptr = ptr.next
            ptr.next = None
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
