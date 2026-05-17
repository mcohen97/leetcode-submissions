'''
[[1,4],[1,2],[2,4]]
[[1,5][4,6][5,7]]
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0 
        def overlaps(intA, intB):
            return intA[1] > intB[0]

        intervals.sort(key=lambda x: x[0])

        i = 1
        cur = intervals[0]
        while i < len(intervals):
            if overlaps(cur, intervals[i]):
                if cur[1] > intervals[i][1]:
                    cur = intervals[i]
                res += 1
            else:
                cur = intervals[i]
            
            i += 1
        
        return res
