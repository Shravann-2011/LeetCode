# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        

        dummy = ListNode(0)

        dummy.next = head

        prevLeft = dummy

        for _ in range(1,left):
            prevLeft = prevLeft.next
        
        curr = prevLeft.next
        prev = None

        for _ in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        leftNode = prevLeft.next
        prevLeft.next = prev
        leftNode.next = curr
        return dummy.next
