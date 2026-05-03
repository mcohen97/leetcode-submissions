class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges) + 1) ]
        rank = [ 1 for i in range(len(edges) + 1) ]

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                rank[node] = rank[par[node]]
                node = par[node]
            return par[node]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] >= rank[rootB]:
                par[rootB] = rootA
            else:
                par[rootA] = rootB

            rank[rootB] += rank[rootA]
            rank[rootA] = rank[rootB]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []



        