class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        
        
        heap = []
        for i in range(k):
            heapq.heappush(heap, -nums[i])
        
        l = 0
        r = k

        result = [-heap[0]]

        while r < len(nums):
            heap.remove(-nums[l])
            heapq.heapify(heap)
            heapq.heappush(heap, -nums[r])

            curMax = -heap[0]
            result.append(curMax)
            
            l += 1
            r += 1
            

        return result

        