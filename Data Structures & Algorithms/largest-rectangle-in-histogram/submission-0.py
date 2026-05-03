class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for pos, height in enumerate(heights): 
            startPos = pos
            while len(stack) > 0 and stack[-1][0] > height:
                prevHeight, prevPos = stack.pop()
                previousBlockArea = prevHeight * (pos - prevPos)
                maxArea = max(previousBlockArea, maxArea)
                startPos -= 1
            stack.append((height, startPos))

        while len(stack) > 0:
            areaUntilTheEnd = stack[-1][0] * (len(heights) - stack[-1][1])
            maxArea = max(areaUntilTheEnd, maxArea)
            stack.pop()

        return maxArea

                
                