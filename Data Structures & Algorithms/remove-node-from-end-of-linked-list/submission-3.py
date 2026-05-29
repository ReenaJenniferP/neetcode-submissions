# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count = 0 

        # curr = head
        # while curr:
        #     curr = curr.next
        #     count += 1

        # count -= n

        # if count == 0:
        #     return head.next

        # curr = head 
        # prev = head
        # while count > 0:
        #     prev = curr
        #     curr = curr.next
        #     count -= 1 

        # prev.next = curr.next
        
        # return head

        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
