'''

Intuition: 

Process one task at a time -> queue
Duplicated tasks

We need to deprioritise tasks that have been recently processed:
 - Priority queue

 How to track the passage of time, how do we determine an idle.

 Inverse-priority queue, 1 is highest priority.
 Priority = from what timestamp this task can be processed

 Binary heap


 Solution:


 - Group tasks by type and add frequency to them
 - Initiate a Heap PQ with some inverse priority, and all the items have priority 1 (order doesn't matter)
 - Clock set to time 1

 - While PQ not empty: 
    - process a task 
    - reduce the count of a task, if 0, we remove
      if not 0, we assign priority = clock + n
    - move clock 1 cycle

 Arrange in frequency groups -> time O(N)
 Heapify -> time O(N)
 Process all tasks. Worst  nlogn (process + update priorityes) + n*m (busy waiting) WORST CASE
 n (m + logn)

 Space O(N)
 
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = collections.Counter(tasks)

        clock = 0

        pq = list(map(lambda task: (0, task[0], task[1]), taskFreq.items()))

        heapq.heapify(pq)

        while pq:
            nextTask = pq[0]

            if nextTask[0] <= clock:
              (notBefore, task, count) = heapq.heappop(pq)
              if count > 1: # Re insert
                count -= 1
                heapq.heappush(pq, (notBefore + n + 1, task, count))

            clock += 1

        return clock
        


        