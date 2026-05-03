# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque([root])

        while q:
            res.append(list(map(lambda n : n.val, q)))

            for i in range(len(q)):
                curNode = q.popleft()

                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)

        
        return res
