# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    class State:
        def __init__(self, diameter=0):
            self.diameter = diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       state = self.State()

       self.diameterOfBinaryTreeRec(root, state)

       return state.diameter

    
    def diameterOfBinaryTreeRec(self, root: Optional[TreeNode], state: State) -> int:
        if not root:
            return 0

        hl, hr = self.diameterOfBinaryTreeRec(root.left, state), self.diameterOfBinaryTreeRec(root.right, state)

        state.diameter = max(state.diameter, hl + hr)

        return 1 + max(hl, hr)

   


