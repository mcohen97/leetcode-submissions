# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # returns kthSmallest if found, and elements count
        def dfs(root, k):
            if not root:
                return None, 0
            
            kthSmallestL, countL = dfs(root.left, k)

            if kthSmallestL:
                return kthSmallestL, None
            
            currentNodePos = countL + 1

            if currentNodePos == k:
                return root, None

            kthSmallestR, countR = dfs(root.right, k - currentNodePos)
            
            if kthSmallestR:
                return kthSmallestR, None

            return None, countL + countR + 1

        kthSmallest, count = dfs(root, k)
        return kthSmallest.val        