# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        before = dummy
        for _ in range(left-1):
            before = before.next
        
        prev = None
        curr = before.next

        for _ in range(right-left+1):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        tail = before.next
        before.next = prev
        tail.next = curr

        return dummy.next