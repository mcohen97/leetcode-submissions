class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        maxL = height[0]
        maxR = height[len(height) - 1]
        trapped = 0

        # [0,2,0,3,1,0,1,3,2,1]

        while left < right:
            if maxL <= maxR:
                left += 1
                if left != 0:
                    trapped += max(maxL - height[left], 0)
                maxL = max(maxL, height[left])
                
            else:
                right -= 1
                if right != len(height) -1:
                    trapped += max(maxR - height[right], 0)
                maxR = max(maxR, height[right])                
        return trapped
                 

