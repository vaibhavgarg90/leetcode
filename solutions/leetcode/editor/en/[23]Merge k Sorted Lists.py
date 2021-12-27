# You are given an array of k linked-lists lists, each linked-list is sorted in 
# ascending order. 
# 
#  Merge all the linked-lists into one sorted linked-list and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#  
# 
#  Example 2: 
# 
#  
# Input: lists = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: lists = [[]]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] is sorted in ascending order. 
#  The sum of lists[i].length won't exceed 10^4. 
#  
#  Related Topics Linked List Divide and Conquer Heap (Priority Queue) Merge 
# Sort 👍 9696 👎 411


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#import heapq

#from faust.models.typing import ListNode


def __lt__(self, other):
    return self.val <= other.val

ListNode.__lt__ = __lt__

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ptr = ListNode()
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        heapq.heapify(heap)
        while heap:
            val, node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
