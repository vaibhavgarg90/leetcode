# Given the head of a singly linked list, sort the list using insertion sort, 
# and return the sorted list's head. 
# 
#  The steps of the insertion sort algorithm: 
# 
#  
#  Insertion sort iterates, consuming one input element each repetition and 
# growing a sorted output list. 
#  At each iteration, insertion sort removes one element from the input data, 
# finds the location it belongs within the sorted list and inserts it there. 
#  It repeats until no input elements remain. 
#  
# 
#  The following is a graphical example of the insertion sort algorithm. The 
# partially sorted list (black) initially contains only the first element in the 
# list. One element (red) is removed from the input data and inserted in-place into 
# the sorted list with each iteration. 
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
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
#  Related Topics Linked List Sorting 👍 1813 👎 780


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        curr = head.next
        while curr is not None:
            curr_next = curr.next
            if curr.val < head.val:
                curr.next = head
                head = curr
                last.next = curr_next
            else:
                last_next = last.next
                last.next = None
                tmp = head
                while tmp.next and tmp.next.val <= curr.val:
                    tmp = tmp.next
                if tmp.next:
                    tmp_next = tmp.next
                    tmp.next = curr
                    curr.next = tmp_next
                    last.next = curr_next
                else:
                    last.next = last_next
                    last = curr
            curr = curr_next
        return head
# leetcode submit region end(Prohibit modification and deletion)
