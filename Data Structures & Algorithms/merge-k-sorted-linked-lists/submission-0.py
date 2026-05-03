# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = ListNode(0)

        mh = []

        for pos, l in enumerate(lists):
            if l:
                heapq.heappush(mh, (l.val, pos, l))
        
        while mh:
            _, pos, listWithSmallerHeadValue = heapq.heappop(mh)
            tail.next = listWithSmallerHeadValue
            listWithSmallerHeadValue = listWithSmallerHeadValue.next
            tail = tail.next
            tail.next = None
            if listWithSmallerHeadValue:
                heapq.heappush(mh, (listWithSmallerHeadValue.val, pos, listWithSmallerHeadValue))

        return head.next
        
        




        