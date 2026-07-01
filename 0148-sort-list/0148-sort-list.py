# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()

        i = 0
        temp = head
        while temp:
            temp.val = arr[i]
            i+=1
            temp= temp.next
        return head
