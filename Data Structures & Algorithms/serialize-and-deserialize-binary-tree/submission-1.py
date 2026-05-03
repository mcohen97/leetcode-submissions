# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque()
        q.append(root)

        sol = []
        level = 0

        while q:
            levelSize = 2**level

            nextLevelHasValue = False
            for i in range(levelSize):
                cur = q.popleft()
                if not cur:
                    sol.append("null")
                    q.append(None)
                    q.append(None)
                else:
                    sol.append(str(cur.val))
                    q.append(cur.left)
                    q.append(cur.right)
                    nextLevelHasValue = nextLevelHasValue or cur.left or cur.right

            if not nextLevelHasValue:
                print("SERIALIZED: ", ",".join(sol))
                return ",".join(sol)
            
            level += 1
        
        return None
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = "0," + data
        nodes = data.split(",")
        print("Nodes", nodes)

        def dfs(nodes, cur):
            if cur >= len(nodes):
                return None

            currentNode = nodes[cur]

            if currentNode == 'null':
                return None
            
            root = TreeNode(currentNode)
            root.left = dfs(nodes, 2 * cur)
            root.right = dfs(nodes, 2 * cur + 1)

            return root


        return dfs(nodes, 1)


