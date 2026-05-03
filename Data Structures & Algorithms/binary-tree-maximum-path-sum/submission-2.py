# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')

        def dfs(root):
            nonlocal maxPath

            if not root:
                return 0
            
            maxPathL = dfs(root.left)
            maxPathR = dfs(root.right)

            maxPath = max(
                maxPath, 
                root.val, 
                root.val + maxPathL, 
                root.val + maxPathR,
                root.val + maxPathR + maxPathL
            )

            return root.val + max(maxPathL, maxPathR, 0)

        dfs(root)
        return maxPath


        