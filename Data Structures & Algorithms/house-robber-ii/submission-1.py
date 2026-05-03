class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = nums[-1], 0
        n = len(nums)

        for i in range(n - 2, 0, -1):
            tmp = max(rob1, nums[i] + rob2)
            rob2 = rob1
            rob1 = tmp
        
        sol1 = rob1

        rob1, rob2 = nums[-2], 0

        for i in range(n - 3, -1, -1):
            tmp = max(rob1, nums[i] + rob2)
            rob2 = rob1
            rob1 = tmp
        
        return max(rob1, sol1)
        