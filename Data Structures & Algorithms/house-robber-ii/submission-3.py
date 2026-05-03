class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1 = [0 for num in nums] # Ignore first one
        dp2 = [0 for num in nums] # Ignore last one

        dp1[1] = nums[1] 

        for i in range(2, len(nums)):
            dontStealI = dp1[i - 1]
            stealI = nums[i] + dp1[i - 2]
            dp1[i] = max(dontStealI, stealI)
        
        dp2[0] = nums[0]

        for j in range(1, len(nums) - 1):
            dontStealJ = dp2[j - 1]
            stealJ = nums[j] + dp2[j - 2] if j >= 2 else nums[j]
            dp2[j] = max(dontStealJ, stealJ)
        
        return max(dp1[-1], dp2[-2])

        

         

        