# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def dfs(root, p, q):
            if not root:
                return None, None

            lca, nodeFoundL = dfs(root.left, p, q)

            if lca:
                return lca, None
            
            lca, nodeFoundR = dfs(root.right, p, q)

            if lca:
                return lca, None
            
            if nodeFoundL and nodeFoundR or ((nodeFoundL or nodeFoundR) and (root.val == p.val or root.val == q.val)):
                return root, None

            if nodeFoundL:
                return None, nodeFoundL
            
            if nodeFoundR:
                return None, nodeFoundR
            
            if root.val == p.val or root.val == q.val:
                return None, root

            return None, None
            


        lca, _ = dfs(root, p, q)

        return lca        