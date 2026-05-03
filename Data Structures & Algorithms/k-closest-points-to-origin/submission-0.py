class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(point: List[int]):
            return math.sqrt(point[0]**2 + point[1]**2)

        l, r = 0, len(points) - 1

        while l < r:
            pivot = r
            aux = l - 1

            for j in range(l, pivot):
                if dist(points[j]) < dist(points[pivot]):
                    aux += 1 
                    points[aux], points[j] = points[j], points[aux]

            
                
            aux += 1
            points[aux], points[pivot] = points[pivot], points[aux]
            pivot = aux

            if pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1

        return points[:k]

            




