class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set(nums)
        list = []
        left = min(nums_set)
        right = max(nums_set)
        for i in range(left,right):
            if i not in nums_set:
                list.append(i)
        return list

        


        