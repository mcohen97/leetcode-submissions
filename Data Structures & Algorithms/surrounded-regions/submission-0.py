'''
Input is a matrix with only X and 'O' characters.
Output is none, we just update the array placing X for every group of connected Os sorrounded by X

assumptions: sorrounded is in the up-down-left-right axises


intuitions

- we can't know the size of a group, but it's possible to explore it recursively
- I wonder if we could do DFS on each cell of this matrix, we could expand every time we find O's and know if it's sorrounded
- In this case, sorrounded means that the group of connecrted O's is not touching any of the  borders I guess, this condition is sufficient.

Proposed solution

For every O found, we do DFS. In the DFS we expand every time we see and adjacent O. We use some set/memory structure to keep the visited cells and avoid any infinite loop
We can know that a group is not sorrounded if one of the Os is touching the border, so we can know if one group is sorrounded or not.
Once we do that and we find a sorrounding group, we can replace the Os in a second roind

analysis:

2 M x N
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def flood(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return

            board[r][c] = 'A'

            for y, x in directions:
                flood(r + y, c + x)

        for i in range(ROWS):
            flood(i, 0)
            flood(i, COLS - 1)

        for j in range(COLS):
            flood(0, j)
            flood(ROWS - 1, j)


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'A':
                    board[i][j] = 'O'


                
            
            

            



        





        
        