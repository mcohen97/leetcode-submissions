# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        res = 0
        path = [root.val]

        def dfs(node):
            if not node:
                return
            
            prevMax = path[-1]

            if node.val >= prevMax:
                nonlocal res
                res += 1
            
            path.append(max(prevMax, node.val))

            dfs(node.left)
            dfs(node.right)

            path.pop()

        dfs(root)
        return res

