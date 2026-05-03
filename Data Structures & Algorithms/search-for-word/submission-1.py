'''
Intuition:

ws(i, j, w)
    if matrix[i][j] == w[0]:
        ws(i, j + 1, w[1:]) or ws(i + 1, j, w[1:])


ws(i, j, w)
       ws(i, j + 1, w[1:]) or ws(i + 1, j, w[1:]) 

 

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def bt(i, j, w, visited):
            if not w:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            if (i, j) in visited:
                return False
            
            letter = board[i][j]
            

            found = False

            visited.add((i, j))
            if w[0] == letter:
                found = (bt(i - 1, j, w[1:], visited) or bt(i + 1, j, w[1:], visited) or bt(i, j - 1, w[1:], visited)  or bt(i, j + 1, w[1:], visited))

            found = found or (bt(i - 1, j, word, visited) or bt(i + 1, j, word, visited) or bt(i, j - 1, word, visited)  or bt(i, j + 1, word, visited))
            
            visited.remove((i, j))
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                found = bt(i, j, word, set())
                if found:
                    return True
        return False
            

        