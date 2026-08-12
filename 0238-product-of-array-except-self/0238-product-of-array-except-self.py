class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        answer[0] = 1
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]

        rightProd = 1
        for i in range(n-1,-1,-1):
            answer[i] *= rightProd
            rightProd *= nums[i]
        return answer

