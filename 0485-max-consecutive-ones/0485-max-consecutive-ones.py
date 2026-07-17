class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_ans = 0
        j = 0
        while j < len(nums):
            if nums[j] == 1:
                j+=1
                current_count+=1
                max_ans = max(max_ans,current_count)
            else:
                j+=1
                current_count = 0
        return max_ans

        