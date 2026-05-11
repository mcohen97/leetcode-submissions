class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [None for i in range(len(s) + 1)]
        dp[0] = True

        tokens = []
        for i in range(len(p)):
            if i < len(p) - 1 and p[i + 1] == '*':
                tokens.append(p[i:i + 2])
            elif p[i] != '*':
                tokens.append(p[i])

        print(tokens)
        
        for token in tokens:
            cur = [None for i in range(len(s) + 1)]

            for i in range(len(cur)):
                match = token[0] == '.' or token[0] == s[i - 1]

                if len(token) == 2:
                    if match:
                        cur[i] = cur[i - 1] or dp[i]
                    else:
                        cur[i] = dp[i]
                elif match:
                    cur[i] = dp[i - 1]
                else: 
                    cur[i] = False            
            dp = cur
        
        return dp[-1] if dp[-1] is not None else False

