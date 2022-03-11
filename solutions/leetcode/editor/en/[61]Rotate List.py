# Given the head of a linked list, rotate the list to the right by k places. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 500]. 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 10⁹ 
#  
#  Related Topics Linked List Two Pointers 👍 4459 👎 1251


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        k = k % n
        if k == 0:
            return head
        ptr = head
        for _ in range(n - k - 1):
            ptr = ptr.next
        res = ListNode()
        tmp = res
        ptr_next = ptr.next
        ptr.next = None
        ptr = ptr_next
        while ptr:
            ptr_next = ptr.next
            tmp.next = ptr
            tmp = ptr
            ptr = ptr_next
        tmp.next = head
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
