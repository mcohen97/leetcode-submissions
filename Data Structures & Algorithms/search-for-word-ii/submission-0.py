class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()

        for word in words:
            cur = trie
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        visited = [[False for x in board[0]] for y in board]

        res = set()

        curWord = ""

        def dfs(i, j, trieNode):
            nonlocal curWord, visited
            
            # print(i, j, curWord)


            if trieNode.endOfWord:
                res.add(curWord)

            # Boundaries
            if (i < 0 or i >= len(board) 
                or j < 0 or j >= len(board[0])):
                return False

            # Visited
            if visited[i][j]:
                return False

            letter = board[i][j]
            if letter not in trieNode.children:
                return False
            
            visited[i][j] = True
            curWord += letter

            dfs(i, j + 1, trieNode.children[letter])
            dfs(i, j - 1, trieNode.children[letter])
            dfs(i + 1, j, trieNode.children[letter])
            dfs(i - 1, j, trieNode.children[letter])

            visited[i][j] = False
            curWord = curWord[:-1]
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie)

        return list(res)