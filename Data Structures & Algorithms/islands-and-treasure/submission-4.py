'''
Clarifications/assumptions:
only move up, down, left, right

Intuitions:


'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = collections.deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        def processPosition(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if grid[i][j] == -1 or grid[i][j] == 0:
                return

            if (i, j) in visited:
                return
            
            visited.add((i, j))

            grid[i][j] = level

            q.append((i, j))

        
        level = 1

        while q:
            # Expand level

            for k in range(len(q)):
                (i, j) = q.popleft()
                processPosition(i + 1, j)
                processPosition(i - 1, j)
                processPosition(i, j + 1)
                processPosition(i, j - 1)
            
            level += 1
            
            


        



        
