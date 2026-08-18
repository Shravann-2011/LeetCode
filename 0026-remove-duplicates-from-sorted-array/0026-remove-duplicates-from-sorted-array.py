class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        for right in range(1,len(nums)):
            if nums[left]!= nums[right]:
                left+=1
                nums[left] = nums[right]
        return left + 1