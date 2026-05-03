# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = ListNode(0)

        while head:
            checkKremaining = head

            i = 1
            while i < k:
                checkKremaining = checkKremaining.next
                if not checkKremaining:
                    last.next = head
                    return first.next
                i += 1

            groupF = groupL = None
            for i in range(k):
                tmp = head
                head = head.next

                if not groupF:
                    groupF =  groupL = tmp
                    tmp.next = None
                else:
                    tmp.next = groupF
                    groupF = tmp
                
            last.next = groupF
            last = groupL

        return first.next

            


        