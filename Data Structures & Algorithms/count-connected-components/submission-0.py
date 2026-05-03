class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                dfs(nei)
            

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = 0
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                visited.add(node)
                res += 1
        
        return res
