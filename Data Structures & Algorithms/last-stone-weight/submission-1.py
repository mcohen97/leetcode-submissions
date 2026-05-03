'''
Can there be only one stone? Yes
Can there be stones with 0 weight? No
Can the list be empty or null? No

Simplify:
We get an array of integers as an input representing stones and their weights
We keep crashing the 2 heaviest ones until we only have one or zero
The output is the remaining stone or 0 if no stones remain

[2,3,6,2,4]
[2,3,2,2,2]
[1, 2, 2, 2]
[1, 2]
[1]

Intuition:

Brute force, finde 2 largest stones O(2N), crash them, insert the remaining oe O(1)
Complexity O(2N^2)

How can we do better than this?

Well, so we see that getting the largest and second largest is a regular thing, so we could rely on some mechanism to get this as quick as possible
'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = list(map(lambda s: -s, stones)) # O(N)

        heapq.heapify(maxHeap) # O(N)

        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap) # O(LogN)
            secondHeaviest = -heapq.heappop(maxHeap) # O(LogN)

            if heaviest == secondHeaviest:
                continue

            heapq.heappush(maxHeap, -(heaviest - secondHeaviest)) # O(LogN)
        
        return -maxHeap[0] if maxHeap else 0
        






        