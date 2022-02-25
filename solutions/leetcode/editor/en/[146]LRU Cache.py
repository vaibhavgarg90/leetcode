# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise 
# return -1. 
#  void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
# the capacity from this operation, evict the least recently used key. 
#  
# 
#  The functions get and put must each run in O(1) average time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10⁴ 
#  0 <= value <= 10⁵ 
#  At most 2 * 10⁵ calls will be made to get and put. 
#  
#  Related Topics Hash Table Linked List Design Doubly-Linked List 👍 12198 👎 4
# 78


# leetcode submit region begin(Prohibit modification and deletion)
class Node(object):
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        node_str = f"key <=> {self.key}, val <=> {self.val}"
        node_str += f", prev <=> {None if not self.prev else self.prev.key}"
        node_str += f", next <=> {None if not self.next else self.next.key}"
        return node_str

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(-1)
        self.last = Node(-1)
        self.head.next = self.last
        self.last.prev = self.head

    def move_to_front(self, node):
        # update prev and next of the node
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        # move node to the front
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def insert(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def remove(self):
        node_to_remove = self.last.prev
        node_to_remove_prev = node_to_remove.prev
        node_to_remove_prev.next = self.last
        self.last.prev = node_to_remove_prev
        return node_to_remove

    def __str__(self):
        ptr = self.head.next
        list_str = f"last = {self.last.key}"
        while ptr:
            list_str += f" -> {str(ptr)}"
            ptr = ptr.next
        return list_str

    def __repr__(self):
        return self.__str__()


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.map = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.list.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        is_present = key in self.map
        if is_present:
            node = self.map.get(key)
            node.val = value
            self.list.move_to_front(node)
            return

        if self.count == self.capacity:
            node = self.list.remove()
            self.map.pop(node.key, None)
            self.count -= 1

        node = Node(key=key, val=value)
        self.map[key] = node
        self.list.insert(node)
        self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
