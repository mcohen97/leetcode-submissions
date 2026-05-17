"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



Intuition:

In an idea schedule, no interval overlaps with the rest

We would have to check if at least one meeting overlaps with another.
So a simple way would be for each interval, check if overlaps one of the rest
O(N^2)

But since we know the overlapping has to do with the closing of one interval being adter the start of tanother
we can leverage from sorting.

Sorting would be N Log N, and then, it would just take one iteration to see if an interval
overlaps with any of the adjacent ones
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def overlaps(intA, intB):
            return intA.end > intB.start

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if overlaps(intervals[i-1], intervals[i]):
                return False
        
        return True
