'''
DFS
when converting tree to string, user preorder traversla(root, left, right) 
and recursive function, when encounter None, store N otherwise values


#decode
extract values from res
create a pointer that goes through res
when res is N add None to tree
then use recursive function to add the nodes 






'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                # when encounter N, it means the tree has ended here, so move to another path
                return 
            res.append(str(node.val))
            dfs.left = dfs(node.left)
            dfs.right = dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(str(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()





