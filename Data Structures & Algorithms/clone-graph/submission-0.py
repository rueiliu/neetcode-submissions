'''
clone the graph, scan through each nodes and use dfs search to build neighbors

create hashmap, key(old), value new

then check if node is in hashmap(if exists return the node)
create a copy of the node
use a for loop that goes through the node.neighbor, append dfs function to the new copy.neighbor
then apply dfs function to its neighors





'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldToNew = {}


        def dfs(node):
            if not node:
                return None
            if node in OldToNew:
                return OldToNew[node]

            copy = Node(node.val)
            OldToNew[node] = copy

            for val in node.neighbors:
                copy.neighbors.append(dfs(val))

            return copy

        return dfs(node)




        