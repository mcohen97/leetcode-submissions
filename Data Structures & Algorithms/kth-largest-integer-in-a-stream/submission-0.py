class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = list(map(lambda e: -e, nums))
        heapq.heapify(self.pq)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, -val)

        readd = []
        for i in range(self.k):
            readd.append(heapq.heappop(self.pq))
        kth = readd[-1]
        
        for e in readd:
            heapq.heappush(self.pq, e)

        return -kth

        

        
