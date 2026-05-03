# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedList = None

        while head != None:
            aux = head
            head = head.next
            aux.next = reversedList
            reversedList = aux
        
        return reversedList