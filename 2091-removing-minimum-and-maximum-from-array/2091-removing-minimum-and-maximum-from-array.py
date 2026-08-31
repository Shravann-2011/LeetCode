class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        minindex = nums.index(min(nums))
        maxindex = nums.index(max(nums))

        left = min(minindex,maxindex) 
        right = max(minindex,maxindex)

        #remove from the front

        front = right + 1

        # remove from the back

        back = n - left

        # remove from both front and back

        frontback = (left + 1) + (n - right)

        return min(front,back,frontback)
        