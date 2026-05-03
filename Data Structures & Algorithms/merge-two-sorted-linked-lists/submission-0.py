# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    mergedListHead = None
    mergedListTail = None

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                self.insertAtTheEnd(list1)
                list1 = list1.next
            else:
                self.insertAtTheEnd(list2)
                list2 = list2.next
        
        while list1 is not None:
            self.insertAtTheEnd(list1)
            list1 = list1.next
        
        while list2 is not None:
            self.insertAtTheEnd(list2)
            list2 = list2.next

        return self.mergedListHead

    def insertAtTheEnd(self, listNode: ListNode):
        if self.mergedListHead is None:
            self.mergedListHead = listNode
            self.mergedListTail = listNode
        else:
            self.mergedListTail.next = listNode
            self.mergedListTail = listNode


            
