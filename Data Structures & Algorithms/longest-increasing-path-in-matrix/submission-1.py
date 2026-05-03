class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[None for j in matrix[0]] for i in matrix]
        

        def dfs(i, j):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            
            if dp[i][j]:
                return dp[i][j]

            sol = 1
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for ver, hor in directions:
                if (i + ver >= 0 and i + ver < len(matrix) 
                    and j + hor >= 0 and j + hor < len(matrix[0])
                    and matrix[i + ver][j + hor] < matrix[i][j]):
                    sol = max(sol, dfs(i + ver, j + hor) + 1)

            dp[i][j] = sol
            return sol

        sol = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = dfs(i, j)
                sol = max(sol, dp[i][j])
        
        return sol





            
            
            
            

            
            

