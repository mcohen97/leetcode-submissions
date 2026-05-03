class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(set)

        for [course, pre] in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1
        
        res = []
        visited = set()

        q = collections.deque()

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        while q:
            c = q.pop()
            visited.add(c)
            res.append(c)

            for dep in graph[c]:
                if dep in visited:
                    continue

                indegree[dep] -= 1

                if indegree[dep] == 0:
                    q.append(dep)

        return res if len(res) == numCourses else []

            
         