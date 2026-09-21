# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lenA = 0
        lenB = 0
        a = headA
        b = headB

        while a is not None:
            lenA+=1
            a = a.next
        
        while b is not None:
            lenB+=1
            b = b.next

        a = headA
        b = headB

        while lenA > lenB:
            a = a.next
            lenA-=1

        while lenB > lenA:
            b = b.next
            lenB-=1
        
        while a!=b:
            a = a.next
            b = b.next
        return a
        




