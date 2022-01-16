# Given the head of a linked list, return the list after sorting it in 
# ascending order. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 5 * 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
#  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.
# e. constant space)? 
#  Related Topics Linked List Two Pointers Divide and Conquer Sorting Merge 
# Sort 👍 5703 👎 199


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def find_mid(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(head1, head2):
            res = ListNode()
            tail = res
            while head1 or head2:
                _next = None
                if head1 and head2:
                    if head1.val <= head2.val:
                        _next = head1
                        head1 = head1.next
                    else:
                        _next = head2
                        head2 = head2.next
                elif head1:
                    _next = head1
                    head1 = head1.next
                else:
                    _next = head2
                    head2 = head2.next
                tail.next = _next
                tail = _next
            return res.next

        def merge_sort(head):
            if not head:
                return head
            if head.next:
                mid = find_mid(head)
                head2 = mid.next
                mid.next = None
                head1 = merge_sort(head)
                head2 = merge_sort(head2)
            else:
                head1 = head
                head2 = None
            return merge(head1, head2)

        return merge_sort(head)
# leetcode submit region end(Prohibit modification and deletion)
