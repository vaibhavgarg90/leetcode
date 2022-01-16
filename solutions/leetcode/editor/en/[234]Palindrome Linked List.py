# Given the head of a singly linked list, return true if it is a palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,2,1]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 10⁵]. 
#  0 <= Node.val <= 9 
#  
# 
#  
# Follow up: Could you do it in O(n) time and O(1) space? Related Topics Linked 
# List Two Pointers Stack Recursion 👍 7553 👎 495


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            _next = slow.next
            slow.next = prev
            prev = slow
            slow = _next
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
# leetcode submit region end(Prohibit modification and deletion)
