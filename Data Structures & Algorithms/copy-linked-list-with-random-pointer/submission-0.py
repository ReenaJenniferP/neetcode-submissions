"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tail = head
        new_head = None
        new_tail = new_head
        hashmap = {}

        while tail:
            node = Node(tail.val, None, None)
            hashmap[tail] = node
            if not new_head:
                new_head = node
                new_tail = node
            else:
                new_tail.next = node
                new_tail = new_tail.next
            
            tail = tail.next

        new = new_head
        old = head

        while new:
            new.random = hashmap[old.random] if old.random else None
            new = new.next
            old = old.next

        return new_head
        