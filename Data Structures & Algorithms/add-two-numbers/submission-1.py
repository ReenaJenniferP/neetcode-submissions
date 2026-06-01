# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2

        head = ListNode(0)
        res = head
        c = 0
        s = 0

        while ptr1 or ptr2 or c:
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0

            s = v1 + v2 + c
            c = s//10

            res.next = ListNode(s%10)

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

            res = res.next

        return head.next