class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        k = 1


        while (2 * n) > k * (k-1) :
            num = n  - (k * (k-1)/2)

            if num % k == 0:
                count+=1
            k+=1
        return count

        