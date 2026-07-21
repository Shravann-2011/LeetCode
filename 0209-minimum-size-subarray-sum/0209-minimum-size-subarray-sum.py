class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minans = float('inf')
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum+=nums[right]

            while sum >= target:
                minans = min(minans,right-left+1)
                sum -= nums[left]
                left+=1

        return 0 if minans == float('inf') else minans
