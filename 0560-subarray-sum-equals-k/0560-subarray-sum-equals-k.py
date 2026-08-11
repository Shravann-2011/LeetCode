class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        freq = {0:1}
        for right in range(len(nums)):
            prefix_sum +=nums[right]

            if prefix_sum - k in freq:
                count+=freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum,0)+1

        return count
        