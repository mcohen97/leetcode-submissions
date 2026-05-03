class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]

        for i in range(len(dp)):
            dp[i] = 0
        dp[0] = 1
        
        for coin in coins:
            cur = [0 for i in range(amount + 1)]
            cur[0] = 1
            for j in range(1, len(cur)):
                if coin > j:
                    cur[j] = dp[j]
                else: 
                    cur[j] = cur[j - coin] + dp[j]
            dp = cur

        return dp[-1]
