# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOut = 0
        result = resultEnd =  ListNode(0)

        while l1 and l2:
            localSum = l1.val + l2.val + carryOut
            localSumNode = ListNode(localSum % 10)
            carryOut = localSum // 10

            resultEnd.next = localSumNode
            resultEnd = localSumNode

            l1 = l1.next
            l2 = l2.next

        while l1:
            localSum = l1.val + carryOut
            localSumNode = ListNode(localSum % 10)
            carryOut = localSum // 10
            resultEnd.next = localSumNode
            resultEnd = localSumNode
            l1 = l1.next

        while l2:
            localSum = l2.val + carryOut
            localSumNode = ListNode(localSum % 10)
            carryOut = localSum // 10
            resultEnd.next = localSumNode
            resultEnd = localSumNode
            l2 = l2.next

        if carryOut > 0:
            localSumNode = ListNode(carryOut)
            resultEnd.next = localSumNode
            resultEnd = localSumNode

        return result.next
        