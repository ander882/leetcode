#  Swap nodes in pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return ListNode(head.val)

        # We have at least 2 nodes
        # n1 = head
        n2 = head.next
        
        returnhead = ListNode( n2.val, ListNode( head.val ))
        returntail = returnhead.next

        current = n2.next
        while current:  # current is n1
            if current.next == None: 
                returntail.next = ListNode( current.val )
                break
            n2 = current.next
            returntail.next = ListNode( n2.val, ListNode( current.val ))
            returntail = returntail.next.next
            current = n2.next

        return returnhead
      
