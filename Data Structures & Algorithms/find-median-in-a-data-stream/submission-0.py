class MedianFinder:
    def __init__(self):
        self.firstHalf = []
        self.secondHalf = []
        

    def addNum(self, num: int) -> None:
        if not self.secondHalf:
            heapq.heappush(self.secondHalf, num)
            return
        
        if num >= self.secondHalf[0]:
            heapq.heappush(self.secondHalf, num)
            if len(self.secondHalf) > len(self.firstHalf) + 1:
                heapq.heappush(self.firstHalf, -heapq.heappop(self.secondHalf))
        else:
            heapq.heappush(self.firstHalf, -num)
            if len(self.firstHalf) > len(self.secondHalf) + 1:
                heapq.heappush(self.secondHalf, -heapq.heappop(self.firstHalf))


    def findMedian(self) -> float:
        lf, ls = len(self.firstHalf), len(self.secondHalf)

        if lf == ls:
            return (-self.firstHalf[0] + self.secondHalf[0]) / 2
        
        if lf > ls:
            return -self.firstHalf[0]

        return self.secondHalf[0]
        

        
        