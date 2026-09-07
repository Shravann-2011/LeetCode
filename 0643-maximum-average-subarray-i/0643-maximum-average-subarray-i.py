class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        i = 0
        window_sum = 0
        
        ans = float('-inf')
        for j in range(n):
            window_sum += nums[j]

            while (j - i + 1) > k:
                window_sum -= nums[i]
                i+=1
            
            if (j - i + 1) == k:
                ans = max(ans ,window_sum)
            
        return float(ans) / k




        