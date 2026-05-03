class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)

        for [course, pre] in prerequisites:
            graph[course].add(pre)

        def dfs(course, path):
            if not graph[course]:
                return True

            if course in path:
                return False
            
            path.add(course)

            for dep in graph[course].copy():
                canBeFinished = dfs(dep, path)

                if not canBeFinished:
                    return False

                graph[course].remove(dep)
            
            return True

        for course in range(numCourses):
            path = set()
            canBeCompleted = dfs(course, path)
            if not canBeCompleted:
                return False

        return True
                
            
            
        






        