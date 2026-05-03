class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            #validate row
            rowFilledNumbers = set()
            colFilledNumbers = set()

            for j in range(9):
                rowCell = board[i][j]
                columnCel = board[j][i]

                if rowCell in rowFilledNumbers:
                    return False
                elif rowCell != ".":
                    rowFilledNumbers.add(rowCell)
                
                if columnCel in colFilledNumbers:
                    return False
                elif columnCel != ".":
                    colFilledNumbers.add(columnCel)

        for i in range(3):
            for j in range(3):
                blockFilledNumbers = set()
                for x in range(i * 3, i * 3 + 3):
                    for y in range(j * 3, j * 3 + 3):
                        if board[x][y] in blockFilledNumbers:
                            return False
                        elif board[x][y] != ".":
                            blockFilledNumbers.add(board[x][y])
        
        return True