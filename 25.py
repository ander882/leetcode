# 25 Reverse nodes in K-groups

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        if k == 1: return head

        arry = [0]*k

        engine = head
        caboose = head

        while engine:

            for arryCount in range(k):
                arry[arryCount] = engine.val
                engine = engine.next
                if not engine: break
            
            if arryCount < k-1: break

            for arryCount in range(k-1,-1,-1):
                caboose.val = arry[arryCount]
                caboose = caboose.next

        return head
