# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None: return None

        nitems = [0] * (n+1)
        nindex = 0

        nitems[0] = head
        clist = head

        while clist:
            nitems[nindex] = clist
            nindex += 1
            if nindex == (n+1):
                nindex = 0
            clist = clist.next

        ''' We now have:
        n=3 head = [1,2,3,4,5]
        nitems = [5, 2, 3 4], index points to 2

        n=1 head=[1]
        nitems = [1,#0], index points to #0

        n=1 head=[1,2]
        nitems = [1,2], index points to 1

        n=2 head=[1,2]
        nitems = [1,2, #0], index points to #0
        '''
        
        if nitems[nindex] == 0:
            if nindex == n:
                return head.next
            return None

        # we have the -(n+1)
        # remove the -(n)th (next) node
        # or this node points to the node we want to delete

        temp = nitems[nindex]
        temp.next = temp.next.next

        return head
