class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        graph = collections.defaultdict(list)

        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour == node:
                    return False

                if neighbour == prev:
                    continue
                
                if not dfs(neighbour, node):
                    return False
            
            return True
        
        return dfs(0, 0) and len(visited) == n
                
        