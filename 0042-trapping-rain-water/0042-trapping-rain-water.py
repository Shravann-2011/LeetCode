class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1 
        leftmax = height[left]
        rightmax = height[right]
        water = 0


        while left < right:
            if leftmax < rightmax:
                left+=1
                leftmax = max(leftmax,height[left])
                water += leftmax - height[left]
            else:
                right-=1
                rightmax = max(rightmax,height[right])
                water += rightmax - height[right]
        return water


