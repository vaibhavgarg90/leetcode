# # You are given the head of a singly linked-list. The list can be represented 
# 
# # as: 
# # 
# # 
# # L0 → L1 → … → Ln - 1 → Ln
# # 
# # 
# # Reorder the list to be on the following form: 
# # 
# # 
# # L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# # 
# # 
# # You may not modify the values in the list's nodes. Only nodes themselves 
# may 
# # be changed. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: head = [1,2,3,4]
# # Output: [1,4,2,3]
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: head = [1,2,3,4,5]
# # Output: [1,5,2,4,3]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # The number of nodes in the list is in the range [1, 5 * 10⁴]. 
# # 1 <= Node.val <= 1000 
# # 
# # Related Topics Linked List Two Pointers Stack Recursion 👍 5059 👎 194
# 


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow = fast = head
        prev = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        _next = slow.next
        slow.next = None
        slow = _next
        while slow:
            _next = slow.next
            slow.next = prev
            prev = slow
            slow = _next
        res = ListNode()
        tail = res
        while head or prev:
            head_next = head.next if head else None
            prev_next = prev.next if prev else None
            tail.next = head
            tail.next.next = prev
            tail = prev
            head = head_next
            prev = prev_next
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
