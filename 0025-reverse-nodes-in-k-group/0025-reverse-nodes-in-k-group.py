# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head

        prevGroup = dummy

        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupNext = kth.next

            prev = groupNext
            curr = prevGroup.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return dummy.next

        