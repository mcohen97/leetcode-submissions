'''
Questions, any coin, not oficial coins


Intuition:

- Greedy wouldn't work, eg. amount = 17 [1, 3, 4, 5, 10]


expression = min(1 + f(i, amount - coins[i]), f(i+1, amount))

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for i in range(amount + 1)]

        dp[0] = 0

        for a in range(1, len(dp)):
            for c in coins:
                if amount - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[-1] if dp[-1] != amount + 1 else -1
        