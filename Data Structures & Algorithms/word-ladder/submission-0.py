class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        allWords = [beginWord] + wordList
        graph = { w: set() for w in allWords}

        if endWord not in allWords:
            return 0


        def neighbours(w1, w2):
            foundDifferentLetter = False

            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if foundDifferentLetter:
                        return False
                    foundDifferentLetter = True

            return foundDifferentLetter


        for i in range(len(allWords)):
            for j in range(i, len(allWords)):
                if neighbours(allWords[i], allWords[j]):
                    graph[allWords[i]].add(allWords[j])
                    graph[allWords[j]].add(allWords[i])

        print("Graph", graph)
        
        q = collections.deque()
        q.append((1, beginWord))

        visited = set()
        visited.add(beginWord)

        

        print("Begin word", beginWord)

        while q:
            (dist, w) = q.popleft()

            print("Word", w, dist)
            
            if w == endWord:
                print("End word reached", w)
                return dist

            for nei in graph[w]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((dist + 1, nei))
        
        return 0

    
            


            

        