class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left  = 0
        n = len(nums)
        
        for right in range(n):
            nums[right]*=nums[right]
            right+=1
        nums.sort()
        return nums

