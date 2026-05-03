"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copies = {}

        cur = head

        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy = copies[cur]
            copy.next = copies[cur.next] if cur.next else None
            copy.random = copies[cur.random] if cur.random else None
            cur = cur.next

        return copies[head]       