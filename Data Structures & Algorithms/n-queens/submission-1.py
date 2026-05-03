class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        queens = []

        def bt(i, j):
            if (i >= n or j >= n):
                return
            
            if self.canPlace(i, j, queens):
                queens.append((i, j))

                if len(queens) == n:
                    res.append(self.printMatrix(queens, n))
                else:
                    if j == n - 1:
                        bt(i + 1 , 0)
                    else:
                        bt(i , j + 1)
                    

                queens.remove((i, j))

            if j == n - 1:
                bt(i + 1 , 0)
            else:
                bt(i , j + 1)
        
        bt(0, 0)
        return res

    def printMatrix(self, queens, n):
        sol = []
        for i in range(n):
            row = ""
            for j in range(n):
                if (i, j) in queens:
                    row += "Q"
                else:
                    row += "."
            sol.append(row)
        return sol


    def canPlace(self, i, j, queens):
        for (r, c) in queens:
            if r == i or c == j or abs(r - i) == abs(c - j):
                return False
        return True   


