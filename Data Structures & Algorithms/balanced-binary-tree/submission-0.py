# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
if null -> true

we need to calculate height left subtree
we need to calculate height right subtree
compare heights and see that diff <= 1


Height:

if null -> 0

if not null:
    get height left tree
    get height right tree
    return 1 (current node) + max between left and right heights
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalancedRec(root: Optional[TreeNode]) -> [bool, int]:
            if not root:
                return [True, 0]

            [isLeftBalanced, leftHeight] = isBalancedRec(root.left)

            if not isLeftBalanced:
                return [False, None]
            
            [isRightBalanced, rightHeight] = isBalancedRec(root.right)

            if not isRightBalanced:
                return [False, None]

            return [abs(leftHeight - rightHeight) <= 1, 1 + max(leftHeight, rightHeight)]

        [isBalanced, height] = isBalancedRec(root)

        return isBalanced

