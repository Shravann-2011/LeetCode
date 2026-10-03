# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length+=1
        k%=length

        if k == 0:
            return head

        curr.next = head
        
        steps = length - k
        newcurr = head

        for _ in range(1,steps):
            newcurr = newcurr.next
        newhead = newcurr.next

        newcurr.next = None


        return newhead





