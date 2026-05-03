class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[None for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(dp)):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]

        for j in range(1, len(dp[0])):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]


        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):    
                dp[i][j] = False
                curChar = s3[i + j - 1]

                if s1[i - 1] == curChar:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                if s2[j - 1] == curChar:
                    dp[i][j] = dp[i][j]  or dp[i][j - 1]

        return dp[len(s1)][len(s2)]

            
            
            
            


