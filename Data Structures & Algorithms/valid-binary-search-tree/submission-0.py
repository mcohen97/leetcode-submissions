# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True, None, None

            isLeftBST, minL, maxL = dfs(root.left)

            if not isLeftBST:
                return False, None, None
            
            isRightBST, minR, maxR = dfs(root.right)

            if not isRightBST:
                return False, None, None
            
            isValidBST = (not maxL or maxL.val < root.val) and (not minR or minR.val > root.val)
            
            return isValidBST, minL if minL else root, maxR if maxR else root
            

        
        isValid, minNode, maxNode = dfs(root)

        return isValid


        