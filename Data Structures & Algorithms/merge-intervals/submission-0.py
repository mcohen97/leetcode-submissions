class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=(lambda x: x[0]))
        res = []

        def overlaps(int1, int2):
            return int1[1] >= int2[0]
        
        def merge(int1, int2):
            return [min(int1[0], int2[0]), max(int1[1], int2[1])]
        
        for interval in intervals:
            if res and overlaps(res[-1], interval):
                res[-1] = merge(res[-1], interval)
            else:
                res.append(interval)

        return res