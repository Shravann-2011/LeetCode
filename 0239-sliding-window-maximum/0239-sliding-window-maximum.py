from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        deque_ = deque()
        result = [0] * (n-k+1)

        for right in range(n):
            while deque_ and deque_[0] <= right - k:
                deque_.popleft()
            while deque_ and nums[deque_[-1]] < nums[right]:
                deque_.pop()
            deque_.append(right)

            if right >= k - 1:
                result[right-k+1] = nums[deque_[0]]
        return result
        
        