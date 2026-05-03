'''


'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        maxArea = 0

        def measureIsland(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            
            if visited[i][j] or grid[i][j] == 0:
                return 0

            visited[i][j] = True

            return 1 + measureIsland(i + 1, j) + measureIsland(i - 1, j) + measureIsland(i, j + 1) + measureIsland(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, measureIsland(i, j))
        
        return maxArea
                

        