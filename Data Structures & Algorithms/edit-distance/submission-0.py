class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for j in range(len(word2) + 1)]

        for j in range(len(dp)):
            dp[j] = j

        for i in range(1, len(word1) + 1):
            cur = [0 for j in range(len(word2) + 1)]
            cur[0] = i
            for j in range(1, len(dp)):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = dp[j - 1]
                else:
                    cur[j] = 1 + min(dp[j], cur[j - 1], dp[j - 1])
            dp = cur

        return dp[-1]
        