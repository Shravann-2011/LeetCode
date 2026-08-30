from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = defaultdict(int)

        for i in nums:
            num_count[i]+=1
        
        return max(num_count,key = num_count.get)

        