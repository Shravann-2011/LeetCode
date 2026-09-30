# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head

        # To get to the middle of the linkedlist list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while slow:
            next = slow.next
            slow.next = prev

            prev = slow
            slow = next
        
        ans = 0

        while prev:
            ans = max(ans,head.val+prev.val)
            head = head.next
            prev = prev.next
        
        return ans
        

