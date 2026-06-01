# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
            
        count = 0

        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        mid = (count+1)//2

        curr = head
        while mid > 1:
            curr = curr.next
            mid -= 1
        
        rev_head = curr.next
        curr.next = None

        curr = rev_head
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        rev_head = prev

        curr1 = head 
        curr2 = rev_head

        while curr1 and curr2:
            nex1 = curr1.next
            nex2 = curr2.next
            curr1.next = curr2
            curr2.next = nex1
            curr2 = nex2
            curr1 = nex1
        