class PrefixNode:
    val: str
    children: dict[str, "PrefixNode"]
    exists: bool

    def __init__(self, val, children=None, exists=False):
        self.val = val
        self.children = children if children else {}
        self.exists = exists

class PrefixTree:

    def __init__(self):
        self.trie = PrefixNode("")
        
    def insert(self, word: str) -> None:
        i = 0
        aux = self.trie
        while i < len(word):
            c = word[i]

            if c not in aux.children:
                aux.children[c] = PrefixNode(c, {})

            aux = aux.children[c]

            i += 1

        aux.exists = True
        
    def search(self, word: str) -> bool:
        if not word:
            return True
        
        aux = self.trie

        i = 0
        while i < len(word):
            c = word[i]

            if c not in aux.children:
                return False

            aux = aux.children[c]
            i += 1

        return aux.exists

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        
        aux = self.trie

        print(aux.children)

        i = 0
        while i < len(prefix):
            c = prefix[i]

            if c not in aux.children:
                return False

            aux = aux.children[c]
            i += 1

        return True