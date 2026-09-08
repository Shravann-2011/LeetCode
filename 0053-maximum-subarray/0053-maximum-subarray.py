class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]

        CurSum = 0

        for n in nums:
            if CurSum <0:
                CurSum = 0
            CurSum+=n
            maxSub = max(maxSub,CurSum)
        return maxSub

                