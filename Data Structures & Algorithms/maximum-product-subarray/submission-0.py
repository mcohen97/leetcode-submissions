class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMin, localMax = nums[0], nums[0]

        sol = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            localMax, localMin = max(num, num * localMin, num * localMax), min(num, num * localMin, num * localMax)
            sol = max(localMax, sol)

        
        return sol





