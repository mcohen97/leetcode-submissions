# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# A -> B -> C -> D -> E 
# 


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        reversedSecond = None
        slow.next = None

        print(head)
        print(second)

        while second:
            aux = second
            second = second.next
            aux.next = reversedSecond
            reversedSecond = aux
        
        headAux = head
        while reversedSecond:
            mergeAux = reversedSecond
            reversedSecond = reversedSecond.next
            mergeAux.next = headAux.next
            headAux.next = mergeAux
            headAux = headAux.next.next



            





        