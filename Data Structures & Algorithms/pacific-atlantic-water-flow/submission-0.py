class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q = collections.deque()

        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()

        for i in range(ROWS):
            q.append((i, 0))
            pacific.add((i, 0))            
        
        for i in range(COLS):
            q.append((0, i))
            pacific.add((0, i))


        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while q:
            # Visit 
            (r, c) = q.popleft()
            pacific.add((r, c))

            for (y, x) in directions:
                if r + y < 0 or r + y >= ROWS or c + x < 0 or c + x >= COLS:
                    continue

                if (r + y, c + x) not in pacific and heights[r + y][c + x] >= heights[r][c]:
                    q.append((r + y, c + x))

        atlantic = set()
            
        for i in range(ROWS):
            q.append((i, COLS - 1))
            atlantic.add((i, COLS - 1))     
        
        for i in range(COLS):
            q.append((ROWS - 1, i))
            atlantic.add((ROWS - 1, i))

        while q:
            # Visit 
            (r, c) = q.popleft()
            atlantic.add((r, c))

            for [y, x] in directions:
                if r + y < 0 or r + y >= ROWS or c + x < 0 or c + x >= COLS:
                    continue

                if (r + y, c + x) not in atlantic and heights[r + y][c + x] >= heights[r][c]:
                    q.append((r + y, c + x))
        
        intersection =  list(atlantic.intersection(pacific))

        return list(map(lambda cell: [cell[0], cell[1]], intersection))

        
                
                

        