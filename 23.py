# Merge K linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#from heapq import heapify, heappush, heappop

def new__lt__(self, other):
        return self.val < other.val
setattr(ListNode, '__lt__', new__lt__)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []: return None
        if lists == [[]]: return None
        
        # Creating empty heap
        heap = []
        heapify(heap)

        for lst in lists:
            if isinstance( lst, ListNode ):
                heappush( heap, lst )
        
        if heap == []: return None

        lst = heappop(heap)
        head = current = ListNode( lst.val )
        if lst.next:
            heappush( heap, lst.next )        

        while len(heap):
            lst = heappop( heap )
            current.next = ListNode( lst.val )
            current = current.next
            if lst.next:
                heappush( heap, lst.next )        

        return head
