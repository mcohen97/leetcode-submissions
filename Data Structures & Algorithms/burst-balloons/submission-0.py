class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        dp = {}


        def dfs(i, j):
            if i > j:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            sol = 0
            for c in range(i, j + 1):
                coins = balloons[i - 1] * balloons[c] * balloons[j + 1] + dfs(c + 1, j) + dfs(i, c - 1) 
                sol = max(sol, coins)
            
            dp[(i, j)] = sol
            return sol
        
        res = dfs(1, len(balloons) - 2)
        return res
            
            


        