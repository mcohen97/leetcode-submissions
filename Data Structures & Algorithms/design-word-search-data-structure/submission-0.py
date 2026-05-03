class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        

        def dfs(trie, word, i):
            if i == len(word):
                return trie.endOfWord

            letter = word[i]
            if letter not in trie.children:
                if letter != '.':
                    return False

                for child in trie.children.values():
                    if dfs(child, word, i + 1):
                        return True

                return False
            return dfs(trie.children[letter], word, i + 1)
        
        cur = self.trie
        return dfs(cur, word, 0)