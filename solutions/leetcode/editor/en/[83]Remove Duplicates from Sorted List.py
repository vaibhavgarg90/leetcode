# Given the head of a sorted linked list, delete all duplicates such that each 
# element appears only once. Return the linked list sorted as well. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,1,2]
# Output: [1,2]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 300]. 
#  -100 <= Node.val <= 100 
#  The list is guaranteed to be sorted in ascending order. 
#  
#  Related Topics Linked List 👍 3973 👎 174


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode()
        res.next = head
        tail = head
        prev = head
        head = head.next
        while head:
            _next = head.next
            if head.val != prev.val:
                tail.next = head
                tail = head
                prev = head
            head = _next
        tail.next = None
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
