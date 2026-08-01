class Solution(object):
    def numSubseq(self, nums, target):
        MOD = 1000000007

        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1

        return ans