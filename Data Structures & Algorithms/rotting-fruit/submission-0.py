class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        totalFruit = 0
        rottenFruit = 0

        def processCell(i, j):
            nonlocal rottenFruit

            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if grid[i][j] != 1 or (i,j) in visited:
                return
            
            visited.add((i, j))
            q.append((i, j))
            rottenFruit += 1
            grid[i][j] = 2

        q = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 0:
                    totalFruit += 1
                if grid[i][j] == 2:
                    rottenFruit += 1
                    q.append((i, j))

        minute = 0

        if rottenFruit == totalFruit:
            return minute
        
        while q:
            for k in range(len(q)):
                (i, j) = q.popleft()

                for y, x in directions:
                    processCell(i + y, j + x)

            minute += 1
            
        if rottenFruit == totalFruit:
            return minute - 1

        return -1
