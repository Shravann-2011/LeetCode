class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            charr = str(n)
            product  = 1
            for i in charr:
                product*=int(i)

            if product % t == 0:
                return n
            n+=1


            

        