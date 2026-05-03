'''
Clarifications/assumptions:
grid[i][j] cant be other option than '0' or '1'
grid never empty


Intuitons
iterating the matrix row by row will make it hard to keep the context
ideally if we step in dry land we wanna walk all over to identify all the island surface

Proposed solution
classic matrix iteration
if we stand in land, visit all the adjacent land using recursion and mark the land as visited
if water, we move on

'''



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        islands = 0


        def visitIsland(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if visited[i][j] or grid[i][j] == '0':
                return
            
            visited[i][j] = True
            visitIsland(i + 1, j)
            visitIsland(i - 1, j)
            visitIsland(i, j + 1)
            visitIsland(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    visitIsland(i, j)
                    islands += 1

        return islands
