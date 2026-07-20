class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zerocount = 0
        maxcount = 0
        n = len(nums)
        for right in range(0,n):
            if nums[right] == 0:
                zerocount+=1 
            if zerocount > k:
                if nums[left] == 0:
                    zerocount-=1
                left+=1
        return n - left



        