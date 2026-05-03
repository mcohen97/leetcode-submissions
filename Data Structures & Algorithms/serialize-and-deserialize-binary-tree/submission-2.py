# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = ""

        def dfs(root):
            nonlocal serialized
            if not root:
                serialized += ",N"
            else:
                serialized += "," + str(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return serialized[1:] if serialized != "" else serialized
        

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = 0
        parsed = data.split(",")

        def dfs():
            nonlocal index, parsed
            if index >= len(data):
                return None

            cur = parsed[index]
            index += 1

            if cur == "N":
                return None
            
            root = TreeNode(cur)
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()

            


