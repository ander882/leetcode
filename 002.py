# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        o = ListNode
        h = o
        c = 0

        while l1 is not None or l2 is not None:
            if l1 is None:
                a = 0
            else:
                a=l1.val
            if l2 is None:
                b = 0
            else:
                b=l2.val 
            
            n = a + b + c
            if n > 9:
                c=1
                n=n-10
            else:
                c=0
            
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            h.next = ListNode(n)
            h = h.next

        if c == 1:
            h.next = ListNode(1)
            
        return o.next
