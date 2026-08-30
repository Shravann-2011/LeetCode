class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = []
        numbers = set(nums)
      

        for i in range(1,n+1):
            if i not in numbers:
                ans.append(i)

        return ans
        

