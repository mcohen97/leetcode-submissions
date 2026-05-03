class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[None for i in text2] for j in text1]

        def rec(i1, i2):
            if i1 < 0 or i2 < 0:
                return 0

            if dp[i1][i2]:
                return dp[i1][i2]
            
            val = 0

            if text1[i1] == text2[i2]:
                val = 1 + rec(i1 - 1, i2 - 1)

            val = max(val, rec(i1, i2 - 1), rec(i1 - 1, i2))

            dp[i1][i2] = val
            return val

        rec(len(text1) - 1, len(text2) - 1)
        return dp[len(text1) - 1][len(text2) - 1]

