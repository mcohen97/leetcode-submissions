class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for num in nums:
            nextRow = defaultdict(int)
            for curSum, count in dp.items():
                nextRow[curSum + num] += dp[curSum]
                nextRow[curSum - num] += dp[curSum]
            dp = nextRow
        
        return dp[target]

        